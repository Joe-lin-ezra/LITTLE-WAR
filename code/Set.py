import Player
import Army
import select

##下方為假設玩家可初始化軍隊位置的座標範圍
x1 = 1
y1 = 1
x2 = 4
y2 = 5

def set(player = Player(),i,x,y):##傳入要設定的玩家，極其要設定的該軍隊，即要設定的XY座標
    if(player.army[i].x == NULL & player.army[i].y == NULL):##如果玩家該軍隊尚未被設置將可以進行設置
        if(x>=x1 & x <=x2 & y >= y1 & y<= y2):##如果玩家要設定軍隊的座標再生成區域內
            if():##確認是否生成座標是否不再水面或是山上
                return True
            else:##座標是在水面或山上
                return False
        else:##玩家要設定軍隊的座標不再合法生成區域內
            return False
    else:##已經設置完成的軍隊不可再次設定
        return False
##缺少一個本地端放map資訊的地方