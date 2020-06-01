import Player
import Army
import Move
import math

hp = 10

def atk(player1,player2,armyID,EnermyID,map):##需要傳入自己player與對方player物件，並且傳入攻擊以及被攻擊軍隊的ID
    try:  ##如我軍對已經SET過
        armyID = int(armyID)
        EnermyID = int(EnermyID)
        X = int(player1.army[armyID].x)
        try: ##對方軍隊已經set
            armyID = int(armyID)
            EnermyID = int(EnermyID)
            X = int(player2.army[EnermyID].x)
            if (armyID <= (len(player1.army) - 1)):  ##玩家傭有此軍隊
                if (EnermyID <= (len(player2.army) - 1)):  ##對方傭有此軍隊
                    if (player1.army[armyID].hp >0):  ##玩家軍隊還活著
                        if(player2.army[EnermyID].hp >0): ##對方軍隊活著
                            if(player1.army[armyID].atked == 0):##尚未攻擊
                                range = Move.countRange(player1.army[armyID].x,player1.army[armyID].y,player1.army[EnermyID].x,player1.army[EnermyID].y)
                                if (range <= player1.army[armyID].atkRange):  ##合法攻擊範圍
                                    percent = math.ceil((player1.army[armyID].hp/hp).real)##血量換算百分比
                                    atker = player1.army[armyID].atk*percent##攻擊力依照血量變動
                                    player2.army[EnermyID].hp = player2.army[EnermyID].hp-atker ##敵人血量扣掉計算後的攻擊力
                                    print("攻擊成功")
                                    player1.army[armyID].atked = 1 ##完成攻擊
                                    return True
                                else:  ##非法移動範圍
                                    print("超出攻擊範圍")
                                    return False
                            else:##已經攻擊過了
                                print("已經攻擊完成")
                                return False
                        else:##對方軍隊已死亡
                            print("對方軍隊已死亡")
                            return False
                    else:  ##玩家軍隊已死亡
                        print("玩家軍隊已死亡")
                        return False
                else:  ##對方無此軍隊
                    print("對方無此軍隊")
                    return False
            else:##無此軍隊
                print("玩家無此軍隊")
                return False
        except:
            print("對方的軍隊尚未設置")
            return False
    except:
        print("玩家的軍隊尚未設置")
        return  False