from libraries.client.config import CONST_FILE_TO_SEND, CONST_SERVER_SOCKET_BUFFER_SIZE
from classes.fileTransferPacket import FileTransferPacket
import pickle
import hashlib

def idle(self):
    server_adress = (self.ipAdress, self.comPort)
    print('[INFO] : starting up on {} port {}'.format(*server_adress))
    print('[INFO] : Stablishing connection with server...')

    fileToSend=open(CONST_FILE_TO_SEND, 'rb')
    data = fileToSend.read()    
    md5_returned = hashlib.md5(data).hexdigest()
    fileToSend.close()

    fileToSend=open(CONST_FILE_TO_SEND, 'rb')
    totalMsgs=0
    while fileToSend.read(CONST_SERVER_SOCKET_BUFFER_SIZE-5000):
        totalMsgs=totalMsgs+1
    fileToSend.close()

    self.fileChecksum = md5_returned
    self.totalMsgs = totalMsgs

    comments={
        "checksum" : self.fileChecksum,
        "fileName" : CONST_FILE_TO_SEND,
        "totalMsgs" : self.totalMsgs
    }
    txpackage=FileTransferPacket("txReqStart", comments, "")
    msg = pickle.dumps(txpackage)
    try:
        self.sock.sendto(msg, server_adress)
        self.state="startTransmissionAck"
        print("[INFO] : Start transmission Package Sent...")
    except:
        print("[ERROR] : Start transmission Package could not be sent")
    return True