##此為解碼器，專門解析對方傳過來的資訊
import Commander
import winOrLose
import json


transCommandList = {'event': 3, 'player': 1, 'action': ['set 0 2 1', 'move 0 3 1', 'atk 0 0']}##假設收到的訊息為此dic

def deCoder (transCommandList,ForS,map,player2,player1, mapDetail):## ,player2,player1 ##我方會將對方視為player2，因此player2變成主要攻擊者
    transCommandList = transCommandList["action"]
    for i in range(len(transCommandList)):
        TorF = Commander.inputCommand(player2,player1,ForS,transCommandList[i],map, mapDetail)
    TorF = winOrLose.wOrL(player1)  ##判斷我方是否輸了
    if TorF == True:
        print("你輸了")
        return True
    else:
        print("下一回合")
    for i in range(len(player1.army)):
        if (player1.army[i].moved == 0):  ##扣除油或體力
            player1.army[i].fuel = player1.army[i].fuel - 5
        if (player1.army[i].fuel <= 0):
            player1.army[i].hp = 0
        player1.army[i].moved = 0
        player1.army[i].atked = 0
    return TorF