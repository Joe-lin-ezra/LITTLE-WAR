##此為解碼器，專門解析對方傳過來的資訊
import Commander
import winOrLose


transCommandList = {'event': 3, 'player': 1, 'action': ['set 0 2 1', 'move 0 3 1', 'atk 0 0']}##假設收到的訊息為此dic

def deCoder (transCommandList,ForS,map,player2,player1):## ,player2,player1 ##我方會將對方視為player2，因此player2變成主要攻擊者
    transCommandList = transCommandList["action"]
    for i in range (len(transCommandList)):
        TorF = Commander.inputCommand(player2,player1,ForS,transCommandList[i],map)
    TorF = winOrLose.wOrL(player1)  ##判斷對方是否輸了
    if TorF == True:
        print("你輸了")
    else:
        print("下一回合")

