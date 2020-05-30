import CommandList

##指令判斷
def inputCommand():##輸入指令
    while True:
        command = input("請輸入指令\n")##讀取指令
        comList = command.split()##字串切割，切割成list
        comList[0] = comList[0].upper()
        if(comList[0] == "MOVE"):
            print("玩家要求移動")
        elif(comList[0] == "ATK"):
            print("玩家要求攻擊")
        elif(comList[0] == "SET"):
            print("玩家要求設置軍隊")
        elif(comList[0] == "LEAVE"):
            print("玩家跳出輸入框")
            break
        else:
            print("指令輸入錯誤")
        # print(comList[0])

inputCommand()