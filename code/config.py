IP = '192.168.1.107'
PORT = 25565

from enum import Enum

class RequestType:
    joinevent = 1
    request = 2
    sync = 3
    rank = 4
    map = 5
    ac = 6
    player = 7
    win = 8
