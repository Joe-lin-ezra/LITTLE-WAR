

def wOrL(player):
    counter = 0 ##計算幾隻部隊陣亡
    if(player.hq.hp <= 0):
        return True
    else:
        for i in range(len(player.army)):
            if(player.army[i].hp == 0):
                counter += 1
        if (counter == len(player.army)):
            return True
        else:##對方沒輸
            return False

