from libraries.server.config import CONST_SERVER_SOCKET_BUFFER_SIZE, CONST_SERVER_TEMP_FILE_NAME
from libraries.server.isFileInDb import isFileInDb
from classes.fileTransferPacket import FileTransferPacket
import pickle

def waitingForConnection(self):
    data, client_adress = self.sock.recvfrom(CONST_SERVER_SOCKET_BUFFER_SIZE)
    if data:
        print ("[INFO] : Transmition request received...")
        rxRequest=pickle.loads(data)
        if rxRequest.getTypeOfMsg()=="txReqStart":
            self.fileName=rxRequest.getFileName()
            self.totalMsgs=rxRequest.getTotalMessages()
            self.fileChecksum= rxRequest.getChecksum()
        else:
            print("[ERROR] : Syncronization Lost")
        print ("[INFO] : Checking file existence in the DataBase...")
        # -- Missing implementation of isFileInDb() function --
        if isFileInDb(self.fileChecksum):
            print("[INFO] : File is already in DB: It is not necessary to re-transmit")
            comments={
                "status" : "AlreadyInDbNotTransmit",
                "checksum" : self.fileChecksum
            }
            response=FileTransferPacket("TxReqStartAck", comments,"")
            print('[INFO] : Waiting for client connection')
        else:
            print("[INFO] : File is not in DB; Transmission Accepted")
            self.state="rx"
            comments={
                "status" : "NotInDbStartTransmission",
                "checksum" : self.fileChecksum
            }
            response=FileTransferPacket("TxReqStartAck", comments,"")
            #creating a temporary file to reconstruct sent file
            self.tempFile= open(CONST_SERVER_TEMP_FILE_NAME, 'wb')
        message = pickle.dumps(response)
        self.sock.sendto(message, client_adress)
    return