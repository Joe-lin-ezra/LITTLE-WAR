import Player
import Army
import Move
import math

hp = 10

def atk(player1,player2,armyID,EnermyID,map):##需要傳入自己player與對方player物件，並且傳入攻擊以及被攻擊軍隊的ID
    try:  ##如我軍對已經SET過
        armyID = float(armyID)
        armyID = int(armyID)
        X = int(player1.army[armyID].x)
        try: ##對方軍隊已經set
            armyID = int(armyID)
            if (armyID <= (len(player1.army) - 1)):  ##玩家傭有此軍隊
                if (player1.army[armyID].hp > 0):  ##玩家軍隊還活著
                    if (player1.army[armyID].atked == 0):  ##玩家此軍隊尚未攻擊
                        if (EnermyID != "HQ"):  ##如果不是指定總部
                            EnermyID = float(EnermyID)
                            EnermyID = int(EnermyID)
                            X = int(player2.army[EnermyID].x)
                            if (EnermyID <= (len(player2.army) - 1)):  ##對方傭有此軍隊
                                if (player2.army[EnermyID].hp > 0):  ##對方軍隊活著
                                    range = Move.countRange(player1.army[armyID].x, player2.army[armyID].y,player2.army[EnermyID].x, player1.army[EnermyID].y)
                                    if (range <= player1.army[armyID].atkRange):  ##合法攻擊範圍
                                        percent = math.ceil((player1.army[armyID].hp / hp).real)  ##血量換算百分比
                                        atker = player1.army[armyID].atk * percent  ##攻擊力依照血量變動
                                        player2.army[EnermyID].hp = player2.army[EnermyID].hp - atker  ##敵人血量扣掉計算後的攻擊力
                                        player1.army[armyID].ammo = player1.army[armyID].ammo - 1
                                        player1.army[armyID].atked = 1  ##完成攻擊
                                        print("攻擊成功")
                                        return True
                                else:  ##對方軍隊已死亡
                                    print("對方軍隊已死亡")
                                    return False
                            else:  ##對方無此軍隊
                                print("對方無此軍隊")
                                return False
                        else: ##如果指定總部
                            range = Move.countRange(player1.army[armyID].x, player1.army[armyID].y,player2.hq.x, player2.hq.y)
                            if (range <= player1.army[armyID].atkRange):  ##合法攻擊範圍
                                percent = math.ceil((player1.army[armyID].hp / hp).real)  ##血量換算百分比
                                atker = player1.army[armyID].atk * percent  ##攻擊力依照血量變動
                                player2.hq.hp = player2.hq.hp - atker  ##敵人血量扣掉計算後的攻擊力
                                print("攻擊成功")
                                player1.army[armyID].atked = 1  ##完成攻擊
                                return True
                    else:  ##已經攻擊過了
                        print("此軍隊已經攻擊過")
                        return False
                else:  ##玩家軍隊已死亡
                    print("玩家軍隊已死亡")
                    return False
            else:  ##無此軍隊
                print("玩家無此軍隊")
                return False
        except:
            print("對方的軍隊尚未設置")
            return False
    except:
        print("玩家的軍隊尚未設置")
        return  False