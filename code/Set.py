import Player
import Army
import select
import json
datas = select.selectMap(1)
map = select.constructMap(datas)
# for i in range(len(map)):
#     print(map[i])
## 0:路 1:水 2:山
areas = json.loads(datas)["Player1_Area"]  ##生成區域要判斷
print(type(areas["x1"]))

def set(player ,ForS,i,x,y):##傳入要設定的玩家，極其要設定的該軍隊，即要設定的XY座標
    if ForS == 1:##是player1
        areas = json.loads(datas)["Player1_Area"]  ##生成區域要判斷
    elif ForS == 2:##是player2
        areas = json.loads(datas)["Player2_Area"]  ##生成區域要判斷
    if(player.army[i].x == None & player.army[i].y == None):##如果玩家該軍隊尚未被設置將可以進行設置
        if(x>=areas["x1"] & x <=areas["x2"] & y >= areas["y1"] & y<= areas["y1"]):##如果玩家要設定軍隊的座標再生成區域內
            if(map[x][y]==1):##確認是否生成座標是否不再水面或是山上
                player.army[i].x = x  ##設定軍隊座標
                player.army[i].y = y  ##設定軍隊座標
                return True
            else:##座標是在水面或山上
                print("只能生成在路面")
                return False
        else:##玩家要設定軍隊的座標不再合法生成區域內
            print("只能生成在指定區域")
            return False
    else:##已經設置完成的軍隊不可再次設定
        print("此軍隊已經生成完畢")
        return False