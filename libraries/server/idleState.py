
def idle(self):
    try:
        server_address = (self.ipAdress, self.comPort)
        print('[INFO] : starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)
        print('[INFO] : Waiting for client connection')
        self.state="waitingForConnection"
    except:
        print("[ERROR] : Socket cannot be opened")