from Headquarter import Headquarter


class Player:
    def __init__(self):
        self.army = list()
        self.hq = Headquarter(hp=20, x=None, y=None)
