class Room():
    def __init__(self):
        self.user = []
        self.mapId = 0
        self.playerType = 0
    
    def isfull(self):
        return len(self.user) == 2
    
    def adduser(self,id):
        self.user.append(id)
        return self
        