from config import IP, PORT, RequestType
from _thread import *
import socket
import pickle
import json
from GameRoom import Room
from threading import Thread
import select

d = {'message': "done"}
room = {'room': 1, 'turn': 1}

class Server():
    def __init__(self):
        self.userlist = []
        self.rooms = []
        self.ip = IP
        self.port = PORT
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.bind((IP, PORT))
        except socket.error as e:
            print(e)
        self.s.listen(100)
    
    def loop(self, client, addr):
        while True:
            try:

                data = client.recv(2048).decode('utf-8')

                if data:
                    payload = json.loads(data)
                    print(payload)
            except socket.error:
                break
            if payload['event'] == RequestType.joinevent:
                if len(self.rooms) == 0:
                    self.rooms.append(Room())
                    room['room'] = 1
                    room['turn'] = 1
                    self.userlist[payload['place']].send(bytes(json.dumps(room).encode('utf-8')))
                else:
                    for r in self.rooms:
                        if r.isfull():
                            continue
                        r.adduser(payload['place'])
                        room['room'] = 1
                        room['turn'] = 2
                        self.userlist[payload['place']].send(bytes(json.dumps(room).encode('utf-8')))
                    else:
                        self.rooms.append(Room())
                        room['room'] = len(self.rooms)
                        room['turn'] = 1
                        self.userlist[payload['place']].send(bytes(json.dumps(room).encode('utf-8')))

            if payload['event'] == RequestType.sync:
                for r in self.rooms:
                    if(payload['place'] in r.user):
                        for u in r.user:
                            if u == payload['place']:
                                continue
                            else:
                                payload['place'] = u
                                self.userlist[u].send(bytes(json.dumps(payload).encode('utf-8')))
                                self.userlist[payload['place']].send(bytes(json.dumps(d).encode('utf-8')))
            if payload['event'] == RequestType.rank:
                pay = select.selectRank(payload['ID'])
                print(pay)
                self.userlist[payload['player']].send(bytes(json.dumps(pay).encode('utf-8')))

    def update(self):
        client, addr = self.s.accept()
        print("Connected to:", addr)

        self.userlist.append(client)
        data = {'player': (len(self.userlist)), 'message': 0}
        self.userlist[(len(self.userlist)-1)].send(bytes(json.dumps(data).encode('utf-8')))
        start_new_thread(self.loop, (client, str(addr[1])))

    def send(self, clientId):
        for i in range (len(self.userlist)):
            if self.userlist[i] == clientId:
                print(i)
                self.userlist[clientId].send()
                break


if __name__ == "__main__":
    server = Server()
    print("Waiting for a connection, Server Started")
    while True:
        server.update()
    
    
