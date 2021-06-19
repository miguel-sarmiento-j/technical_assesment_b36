from libraries.client.endTxState import endTx
from libraries.client.waitingTxAckState import waitingTxAck
from libraries.client.txPackageState import txPackage
from libraries.client.startTxAckState import startTransmissionAck
from libraries.client.idleState import idle

import socket

switcher={
    "idle": idle,
    "startTransmissionAck": startTransmissionAck,
    "txPackage": txPackage,
    "waitingTxAck": waitingTxAck,
    "endTx":endTx
}

class clientManager:
    def __init__(self, ipAdress, comPort):
        self.currentPackageId=1
        self.state="idle"
        self.ipAdress=ipAdress
        self.comPort=comPort
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.fileToSend=""
        self.nextChunk=""
        self.fileChecksum=""
        self.totalMsgs=0

    def attend(self):
        state = switcher.get(self.state, "Wrong State")
        return state(self)
