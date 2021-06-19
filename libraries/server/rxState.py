from libraries.server.config import CONST_SERVER_SOCKET_BUFFER_SIZE, CONST_SERVER_TEMP_FILE_NAME
from libraries.server.storeInDB import convert_into_binary, insert_into_database
from classes.fileTransferPacket import FileTransferPacket
import pickle

def rx(self):
    data, client_adress = self.sock.recvfrom(CONST_SERVER_SOCKET_BUFFER_SIZE)
    if data:
        rxRequest=pickle.loads(data)
        if rxRequest.getTypeOfMsg() == "transfering":
            if rxRequest.getMsgId() == self.currentPackageId+1:
                self.currentPackageId = self.currentPackageId+1
                self.tempFile.write(rxRequest.getPayload())
                comments={
                    "id"    : rxRequest.getMsgId(),
                    "status" : "OK"
                }
                response=FileTransferPacket("transferingAck", comments,"")
                message = pickle.dumps(response)
                self.sock.sendto(message, client_adress)
                print("[INFO] : ", self.currentPackageId, "/",self.totalMsgs)
            # case ID is not correct
            # elif 
        elif rxRequest.getTypeOfMsg() == "txEnd":
            print("[INFO] : FILE RECEIVED SUCCEFUL!")
            self.tempFile.close()
            file_blob = convert_into_binary(CONST_SERVER_TEMP_FILE_NAME)
            last_updated_entry = insert_into_database(self.fileName, file_blob, self.fileChecksum)
            print("[INFO] : FILE STORED SUCCEFUL!")
            print('[INFO] : Waiting for a new client connection')
            self.currentPackageId=0
            self.state="waitingForConnection"
            self.tempFile=""
            self.fileName=""
            self.fileChecksum=""
            self.totalMsgs=0
        else:
            print("Error in Transmission sequence")
        
    return