from libraries.server.rxState import rx
from libraries.server.waitingForConnectionState import waitingForConnection
from libraries.server.idleState import idle
import socket

switcher={
    "idle": idle,
    "waitingForConnection": waitingForConnection,
    "rx": rx,
}

class ServerManager:
    def __init__(self, ipAdress, comPort):
        self.currentPackageId=0
        self.state="idle"
        self.ipAdress=ipAdress
        self.comPort=comPort
        self.tempFile=""
        self.fileName=""
        self.fileChecksum=""
        self.totalMsgs=0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def attend(self):
        state = switcher.get(self.state, "Wrong State")
        state(self)

