import Move
import Set
import ATK
import Commander
import select
import Player
import Army
import Headquarter
import Constructer ##by Dan

player1 = Player.Player()
player2 = Player.Player()
army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=None,y=None)
player1.army.append(army)
army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=3,y=2)
player2.army.append(army)

player1.hq = Headquarter.Headquarter(hp=20, x=2, y=1)
player2.hq = Headquarter.Headquarter(hp=20, x=2, y=1)

datas = select.selectMap(1)
map = select.constructMap(datas)

transCommandList = {'event':3,'player':1,}##player格子要再改
transComman = []

while True:
    command = input("plz input ur command :\n")
    if (command == "leave"):
        for i in range(len(player1.army)):
            player1.army[i].moved = 0
            player1.army[i].atked = 0
        tmpDic = {"action":transComman}
        transCommandList.update(tmpDic)
        print("下一回合")
        break
    else:
        TorF = Commander.inputCommand(player1, player2, 1, command)  ##這裡應該使GUI呼叫我的地方，我會回傳true or false
        if TorF == True:
            print("記錄下來")
            transComman.append(command)
        else:
            print("不紀錄")
print(transCommandList)
    ##先完善軍隊死亡(血量等於0)
    ##完成紀律指令
    # for i in range(len(map)):
    #     print(map[i])
