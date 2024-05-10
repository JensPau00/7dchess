import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname('10.0.0.215')
        self.port = 80
        self.addr = (self.server, self.port)
        print(self.addr)
        self.pos = self.connect()
        print(13)
        print(self.pos)
        self.pos = self.pos.split(" ")
        self.pos[0] = int(self.pos[0])
    def getPos(self):
        return self.pos
    def connect(self):
        print(11)
        self.client.connect(self.addr)
        print(12)
        return self.client.recv(2048).decode()
    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            pass
def get_move_from_data(data):
    newData = data.split(",")
    return newData
def breakList(sentList, numberOfDimension):
    counter = 0
    sendStr = ""
    sentList = str(sentList)
    print(sentList,'cum')
    for each in sentList:
        try:
            int(each)
            counter+=1
            sendStr+=str(each)
            sendStr += " "
            if counter == numberOfDimension:
                sendStr += ','
        except:
            pass
    print(sendStr)
    return sendStr
