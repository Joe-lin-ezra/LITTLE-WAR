IP = '0.0.0.0'
PORT = 25565

from enum import Enum

class RequestType:
    joinevent = 1
    request = 2
    sync = 3
    rank = 4
