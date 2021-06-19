from classes.fileTransferPacket import FileTransferPacket
import pickle

def endTx(self):
    self.fileToSend.close()
    txpackage=FileTransferPacket("txEnd", "", "")
    msg = pickle.dumps(txpackage)
    try:
        server_adress = (self.ipAdress, self.comPort)
        self.sock.sendto(msg, server_adress)
        self.sock.close()
        print("[INFO] : Transmission Complete!")
    except:
        print("[ERROR] : Start transmission Package could not be sent")
    return False