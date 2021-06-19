from classes.fileTransferPacket import FileTransferPacket
import pickle

def txPackage(self):
    comments={
        "id" : self.currentPackageId
    }
    txpackage=FileTransferPacket("transfering", comments, self.nextChunk)
    #print(self.nextChunk)
    try:
        server_adress = (self.ipAdress, self.comPort)
        msg = pickle.dumps(txpackage)
        self.sock.sendto(msg, server_adress)
        print("[INFO] : ", self.currentPackageId, "/", self.totalMsgs, "packages")
    except:
        print("[ERROR] : Package could not be sent")
    self.state="waitingTxAck"
    #print("txPackage")
    return True