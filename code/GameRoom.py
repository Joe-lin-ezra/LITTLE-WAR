class Room():
    def __init__(self):
        self.user = []
    
    def isfull(self):
        return len(self.user) == 2
    
    def adduser(self,id):
        self.user.append(id)
        