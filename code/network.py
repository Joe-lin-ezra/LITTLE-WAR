import socket
import config
import json

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = config.IP
        self.port = config.PORT
        self.addr = (self.server, self.port)
        self.playerInfor = self.connect()

    def getP(self):
        return self.playerInfor

    def connect(self):
        try:
            self.client.connect(self.addr)
            data = self.client.recv(2048).decode('utf-8')
            j = json.loads(data)
            return j
        except:
            pass

    def recv(self):
        data = self.client.recv(2048).decode('utf-8')
        # print(data)
        return data

    def send(self, data):
        try:
            self.client.send(bytes(json.dumps(data).encode('utf-8')))
            return "done"
        except socket.error as e:
            print(e)
