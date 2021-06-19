from libraries.server.rxState import rx
from libraries.server.waitingForConnectionState import waitingForConnection
from libraries.server.idleState import idle

switcher={
    "idle": idle,
    "waitingForConnection": waitingForConnection,
    "rx": rx,
}

def attendModule(self):
    state = switcher.get(self.state, "Wrong State")
    state(self)
