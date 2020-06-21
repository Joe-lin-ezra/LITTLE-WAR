
class Army:
    def __init__(self, type, hp, movement, ammo, fuel, atk, atkRange, vision, x,y):
        self.type = type
        self.hp = hp
        self.movement = movement
        self.ammo = ammo
        self.fuel = fuel
        self.atk = atk
        self.atkRange = atkRange
        self.vision = vision
        self.x = x
        self.y = y
        self.moved = 0 ## 0 尚未移動 1 已經移動
        self.atked = 0 ## 0 尚未攻擊 1 已經攻擊
