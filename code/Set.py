import Player
import Army
import select
import json
# datas = select.selectMap(1)
# map = select.constructMap(datas)
# for i in range(len(map)):
#     print(map[i])
# ## 0:路 1:水 2:山
# datas = select.selectMap(1)
# datas = json.dumps(datas)
# areas = json.loads(datas)["Player1_Area"]  ##生成區域要判斷
# print(type(areas["x1"]))

def set(player,player2 ,ForS,i,x,y,map, datas):##傳入要設定的玩家，極其要設定的該軍隊，即要設定的XY座標 ForS first or second
    try:  ##如我軍對已經SET過
        i = int(i)
        X = int(player.army[i].x)
        print("此軍隊已經生成完畢") ##已經設置完成的軍隊不可再次設定
        return False
    except:##軍隊沒有設置過
        i = float(i)
        i = int(i)
        x = float(x)
        x = int(x)
        y = float(y)
        y = int(y)
        if ForS == 1:##是player1
            areas = datas["Player1_Area"]  ##生成區域要判斷
        elif ForS == 2:##是player2
            areas = datas["Player2_Area"]  ##生成區域要判斷
        if(x>=areas["x1"] and x <=areas["x2"] and y >= areas["y1"] and y<= areas["y2"]):##如果玩家要設定軍隊的座標再生成區域內
            try:##沒超過地圖大小
                if(map[x][y]==0):##確認是否生成座標是否不再水面或是山上
                    for j in range (len(player2.army)):
                        if(player2.army[j].x == x and player2.army[j].y == y):
                            print("與敵人重疊")
                            return False
                    player.army[i].x = x  ##設定軍隊座標
                    player.army[i].y = y  ##設定軍隊座標
                    print(i,x,y)
                    print("X: " + str(player.army[0].x))
                    print("Y: " + str(player.army[0].y))
                    print("設定完成")
                    return True
                else:##座標是在水面或山上
                       print("只能生成在路面")
                       return False
            except:##超過地圖大小
                print("Out of map range")
                return False
        else:##玩家要設定軍隊的座標不再合法生成區域內
            print("只能生成在指定區域")
            return False