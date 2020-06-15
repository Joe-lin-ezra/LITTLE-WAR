from config import IP, PORT, RequestType
from _thread import *
import socket
import json
from GameRoom import Room
import UserSignUp
import updatePlayer
import select
import select
import random

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
        self.s.listen(2)
    
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
                    self.rooms[len(self.rooms) - 1].mapId = random.randint(1, 2)
                    self.rooms[len(self.rooms) - 1].playerType = random.randint(1, 2)
                    self.rooms[len(self.rooms) - 1].user.append(payload['player'])
                    room['room'] = len(self.rooms)
                    room['turn'] = 1
                    self.userlist[payload['player']].send(bytes(json.dumps(room).encode('utf-8')))
                else:
                    for r in self.rooms:
                        if r.isfull():
                            continue
                        self.rooms[len(self.rooms) - 1].user.append(payload['player'])
                        room['room'] = len(self.rooms)
                        room['turn'] = 2
                        self.userlist[payload['player']].send(bytes(json.dumps(room).encode('utf-8')))
                        break
                    else:
                        self.rooms.append(Room())
                        self.rooms[len(self.rooms)-1].mapId = random.randint(1, 2)
                        self.rooms[len(self.rooms) - 1].playerType = random.randint(1, 2)
                        self.rooms[len(self.rooms) - 1].user.append(payload['player'])
                        room['room'] = len(self.rooms)
                        room['turn'] = 1
                        self.userlist[payload['player']].send(bytes(json.dumps(room).encode('utf-8')))

            elif payload['event'] == RequestType.sync:
                u = 0
                for i in range(2):
                    if self.rooms[payload['room']-1].user[i] != payload['player']:
                        u = self.rooms[payload['room']-1].user[i]
                        break
                self.userlist[u].send(bytes(json.dumps(payload).encode('utf-8')))
            elif payload['event'] == RequestType.rank:
                pay = select.selectRank(payload['name'])
                self.userlist[payload['player']].send(bytes(json.dumps(pay).encode('utf-8')))
            elif payload['event'] == RequestType.map:
                map = select.selectMap(self.rooms[(payload['room']-1)].mapId)
                self.userlist[payload['player']].send(bytes(json.dumps(map).encode('utf-8')))
            elif payload['event'] == RequestType.ac:
                if payload['num'] == 1:
                    data = UserSignUp.register(payload['name'])
                    self.userlist[payload['player']].send(bytes(json.dumps(data).encode('utf-8')))
                elif payload['num'] == 2:
                    data = UserSignUp.login(payload['name'])
                    self.userlist[payload['player']].send(bytes(json.dumps(data).encode('utf-8')))
            elif payload['event'] == RequestType.player:
                player = select.selectDeploy(self.rooms[payload['room']-1].mapId)
                self.userlist[payload['player']].send(bytes(json.dumps(player).encode('utf-8')))
            elif payload['event'] == RequestType.win:
                updatePlayer.winTimesUpdate(name=payload['name'])



    def update(self):
        client, addr = self.s.accept()
        print("Connected to:", addr)

        self.userlist.append(client)
        data = {'player': (len(self.userlist)), 'message': 0}
        self.userlist[(len(self.userlist)-1)].send(bytes(json.dumps(data).encode('utf-8')))
        start_new_thread(self.loop, (client, str(addr[1])))

if __name__ == "__main__":
    server = Server()
    print("Waiting for a connection, Server Started")
    while True:
        server.update()
    
    