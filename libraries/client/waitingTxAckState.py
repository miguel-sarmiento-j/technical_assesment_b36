from libraries.client.config import CONST_SERVER_SOCKET_BUFFER_SIZE
import pickle

def waitingTxAck(self):
    data, address = self.sock.recvfrom(CONST_SERVER_SOCKET_BUFFER_SIZE)
    if data:
        TxRequestAck=pickle.loads(data)
        if TxRequestAck.getTypeOfMsg()=="transferingAck" and TxRequestAck.getMsgId()==self.currentPackageId and TxRequestAck.getStatus()=="OK":
            self.nextchunk=self.fileToSend.read(CONST_SERVER_SOCKET_BUFFER_SIZE-5000)
            if not self.nextchunk:
                self.state="endTx"
            else:
                self.state="txPackage"
                self.currentPackageId=self.currentPackageId+1
        else:
            print("[ERROR] : Syncronization Error")
    return True