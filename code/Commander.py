import CommandList
import Move
import Set
import ATK

##test
import select
import Player
import Army
import Headquarter
import Constructer ##by Dan

# player1 = Player.Player()
# player2 = Player.Player()
# army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=3,y=4)
# player1.army.append(army)
# army = Army.Army(type='Infantry', hp=10, movement=1, atk=1, atkRange=1, vision=0, x=5,y=5)
# player2.army.append(army)
#
# player1.hq = Headquarter.Headquarter(hp=20, x=2, y=1)
# player2.hq = Headquarter.Headquarter(hp=20, x=2, y=1)
# if (player1.army[0].moved == 0):
#     print("A")
# ##test


##指令判斷
def inputCommand(player,player2,ForS,command):##輸入指令
    while True:
        comList = command.split()##字串切割，切割成list
        comList[0] = comList[0].upper()
        if(comList[0] == "MOVE"):
            print("玩家要求移動")
            TorF = Move.move(player,comList[1],comList[2],comList[3])##傳入player物件，player的army的ID，以及此軍隊的X和Y
            return TorF
        elif(comList[0] == "ATK"):
            print("玩家要求攻擊")
            TorF = ATK.atk(player,player2,comList[1],comList[2])##需要傳入自己player與對方player物件，並且傳入攻擊以及被攻擊軍隊的ID
            return TorF
        elif(comList[0] == "SET"):
            print("玩家要求設置軍隊")
            ##ForS first or second
            TorF = Set.set(player ,ForS,comList[1],comList[2],comList[3])##傳入要設定的玩家，極其要設定的該軍隊，即要設定的XY座標
            return TorF
        elif(comList[0] == "LEAVE"):
            print(player.army[0].atked)
            print(player.army[0].moved)
            for i in range (len(player.army)):
                player.army[i].moved = 0
                player.army[i].atked = 0
            print("下一回合")
            break
        else:
            print("指令輸入錯誤")
        # print(comList[0])
# while True:
#     command = input("請輸入指令\n")##讀取指令
#     inputCommand(player1,player2,1,command)