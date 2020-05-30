import CommandList
import Move
import Set
import ATK
##指令判斷
def inputCommand(player,player2,ForS):##輸入指令
    while True:
        command = input("請輸入指令\n")##讀取指令
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
            print("玩家跳出輸入框")
            break
        else:
            print("指令輸入錯誤")
        # print(comList[0])

# inputCommand()