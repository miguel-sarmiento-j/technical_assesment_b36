from libraries.client.config import CONST_FILE_TO_SEND, CONST_SERVER_SOCKET_BUFFER_SIZE
import pickle

def startTransmissionAck(self):
    data, address = self.sock.recvfrom(CONST_SERVER_SOCKET_BUFFER_SIZE)
    if data:
        TxRequestAck=pickle.loads(data)
        if TxRequestAck.getTypeOfMsg()=="TxReqStartAck":
            if TxRequestAck.getStatus()=="AlreadyInDbNotTransmit" and TxRequestAck.getChecksum()==self.fileChecksum:
                print("[INFO] : File is already in the database, there is no need to transfer it")
            elif TxRequestAck.getStatus()=="NotInDbStartTransmission" and TxRequestAck.getChecksum()==self.fileChecksum:
                print("[INFO] : Server Response: Start Transmission")
                print("[INFO] : Starting Transmission")
                self.fileToSend=open(CONST_FILE_TO_SEND, 'rb')
                self.nextChunk=self.fileToSend.read(CONST_SERVER_SOCKET_BUFFER_SIZE-5000)
                self.state="txPackage"
            else:
                print("[ERROR] : Syncronization Error")
        else:
            print ("[ERROR] : Syncronization Error")
    return True