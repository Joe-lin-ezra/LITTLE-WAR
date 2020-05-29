import socket
import config
import json

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = config.IP
        self.port = config.PORT
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            data = self.client.recv(2048).decode('utf-8')
            jload = json.loads(data)
            return jload
        except:
            pass

    def recv(self):
        try:
            data = self.client.recv(2048).decode('utf-8')
            pay = json.loads(data)
            return pay
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(bytes(json.dumps(data).encode('utf-8')))
            data = self.client.recv(2048).decode('utf-8')
            payload = json.loads(data)
            return payload
        except socket.error as e:
            print(e)
