import Move
import Set
import ATK
import Commander
import select
import Player
import Army
import Headquarter
import json
import Constructer ##by Dan
import DeCoder
import winOrLose

# player1 = Player.Player()
# player2 = Player.Player()
# army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=3,y=1)
# player1.army.append(army)
# army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=3,y=2)
# player2.army.append(army)
#
# player1.hq = Headquarter.Headquarter(hp=20, x=2, y=1)
# player2.hq = Headquarter.Headquarter(hp=20, x=0, y=0)

player = select.selectDeploy(1)
player = json.dumps(player)
player1 = Constructer.constructPlayer(player)##正確建構玩家物件
player2 = Constructer.constructPlayer(player)

datas = select.selectMap(1)
datas = json.dumps(datas)
map = Constructer.constructMap(datas)
datas = eval(datas)
# print(datas["Player1_HQ"]["x"])
# print(type(datas["Player1_HQ"]["x"]))
player1.hq = Headquarter.Headquarter(hp=20, x=datas["Player1_HQ"]["x"], y=datas["Player1_HQ"]["y"])
player2.hq = Headquarter.Headquarter(hp=20, x=datas["Player2_HQ"]["x"], y=datas["Player2_HQ"]["y"])

transCommandList = {'event':3,'player':1,}##player格子要再改
transComman = []

# for i in range(len(map)):
#     print(map[i])

## run decoder
# transCommandList = {'event': 3, 'player': 1, 'action': ['set 0 2 1', 'move 0 3 1', 'atk 0 0']}##假設收到的訊息為此dic
# DeCoder.deCoder(transCommandList,1,map,player2,player1)

while True:
    print("HQ:",player1.hq.hp,"X: ",player1.hq.x,"Y: ",player1.hq.y)
    for i in range (len(player1.army)):
        print("ID: ",i," HP:",player1.army[i].hp," X: ",player1.army[i].x," Y: ",player1.army[i].y)
    command = input("plz input ur command :\n")
    if (command == "leave"): ##button按下去要做的事情
        for i in range(len(player1.army)):
            player1.army[i].moved = 0
            player1.army[i].atked = 0
        tmpDic = {"action":transComman}
        transCommandList.update(tmpDic)
        TorF = winOrLose.wOrL(player2)##判斷對方是否輸了
        if TorF ==True:
            print("對方輸了")
        else:
            print("下一回合")
            break
    else:
        TorF = Commander.inputCommand(player1, player2, 1, command,map)  ##這裡應該使GUI呼叫我的地方，我會回傳true or false
        if TorF == True:
            print("記錄下來")
            transComman.append(command)
        else:
            print("不紀錄")
print(transCommandList)