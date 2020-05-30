import Player
import Army
import select
import client
import json
datas = select.selectMap(1)
map = select.constructMap(datas)
for i in range(len(map)):
    print(map[i])

areas = json.loads(datas)[]##生成區域要判斷
## 0:路 1:水 2:山

def set(player ,i,x,y):##傳入要設定的玩家，極其要設定的該軍隊，即要設定的XY座標
    if(player.army[i].x == None & player.army[i].y == None):##如果玩家該軍隊尚未被設置將可以進行設置
        if(x>=x1 & x <=x2 & y >= y1 & y<= y2):##如果玩家要設定軍隊的座標再生成區域內
            if(map[x][y]==1):##確認是否生成座標是否不再水面或是山上
                player.army[i].x = x  ##設定軍隊座標
                player.army[i].y = y  ##設定軍隊座標
                return True
            else:##座標是在水面或山上
                return False
        else:##玩家要設定軍隊的座標不再合法生成區域內
            return False
    else:##已經設置完成的軍隊不可再次設定
        return False
##缺少一個本地端放map資訊的地方