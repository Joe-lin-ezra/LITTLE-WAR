import socket
from network import Network
import json
from config import RequestType

run = True
n = Network()
p = n.getP()
place = 0
send = 1
join = False
myturn = False

join_request = {'event': 1, 'place': 0}
rank_request = {'event': 4, 'place': 0}
snapshot_request = {'event': 2, 'place': 0, 'posx': 0.0, 'posy': 0.0}
sync_request = {'event': 3, 'actions': []}
sync_sent = {'event': 3, 'message': 1}

if not p:
    raise RuntimeError('Cannot find server')
else:
    print('Conned')
    place = p['place'] - 1

while True:
    if join == True:
        print(myturn)
        if myturn == True:
            myturn = not myturn
            w = input()
            if (w == "nextturn"):
                sync_sent['place'] = place
                sync_sent['message'] = "Test123"
                a = n.send(sync_sent)
        else:
            print(1)
            b = n.recv()
            print(b)
            myturn = not myturn

    elif join == False:
        w = input()
        if (w == "join"):
            join = True
            join_request['place'] = place
            a = n.send(join_request)
            if a['turn'] == 1:
                myturn = True
            print('message: ' + str(a))
        elif (w == "rank"):
            rank_request['place'] = place
            a = n.send(join_request)
            print('message: ' + str(a))