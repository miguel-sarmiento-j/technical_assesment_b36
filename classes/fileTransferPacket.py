class FileTransferPacket:
    def __init__(self, typeOfMsg, comments, payload):
        self.typeOfMsg=typeOfMsg
        self.comments=comments
        self.payload=payload
        
    def getTypeOfMsg(self):
        return self.typeOfMsg

    def getChecksum(self):
        if self.typeOfMsg == "txReqStart" or self.typeOfMsg == "TxReqStartAck":
            return self.comments["checksum"]
        else:
            print("[ERROR] :< ",self.typeOfMsg, "type of message does not have checksum field")
            return "err"
    
    def getFileName(self):
        if self.typeOfMsg == "txReqStart":
            return self.comments["fileName"]
        else:
            print("[ERROR] :< ",self.typeOfMsg, "type of message does not have fileName field")
            return "err"

    def getTotalMessages(self):
        if self.typeOfMsg == "txReqStart":
            return self.comments["totalMsgs"]
        else:
            print("[ERROR] :< ",self.typeOfMsg, "type of message does not have totalMsgs field")
            return "err"
    
    def getStatus(self):
        if self.typeOfMsg == "TxReqStartAck":
            return self.comments["status"]
        else:
            print("[ERROR] :< ",self.typeOfMsg, "type of message does not have status field")
            return "err"

    def getMsgId(self):
        if self.typeOfMsg == "transfering":
            return self.comments["id"]
        else:
            print("[ERROR] :< ",self.typeOfMsg, "type of message does not have id field")
            return "err"

    def getPayload(self):
        return self.payload