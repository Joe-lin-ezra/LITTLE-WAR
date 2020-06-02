import Player
import cmath
import math
import select
import Army

##尚未增加耗油部分

# datas = select.selectMap(1)
# map = select.constructMap(datas)
# for i in range(len(map)):
#     print(map[i])
# print(map[2][2])
# a = [0,1,2,3]



def countRange(armyX,armyY,distanceX,distanceY):
       range = cmath.sqrt((armyX - distanceX) * (armyX - distanceX) + (armyY - distanceY )* (armyY - distanceY))
       range = math.ceil(range.real)
       return range

# while True:  ##debug
#     armyX = int(input("x1\n"))
#     armyY = int(input("y1\n"))
#     distanceX = int(input("x2\n"))
#     distanceY = int(input("y2\n"))
#     countRange(armyX,armyY,distanceX,distanceY)

def move(player,player2,i,x,y,map):## x y 是要過去的座標
       road = 0 ##定義路面數字
       try:##如我軍對已經SET過
              i = float(i)
              i = int(i)
              x = float(x)
              x = int(x)
              y = float(y)
              y = int(y)
              X = int(player.army[i].x)
              if (i <= (len(player.army) - 1)):  ##傭有此軍隊
                     if (player.army[i].hp > 0):  ##軍隊還活著
                            if (player.army[i].moved == 0):  ##選擇的士兵尚未移動
                                   if (map[x][y] == road):  ##是可以到達的地形
                                          rang = countRange(player.army[i].x, player.army[i].y, x, y)  ##計算軍隊到目的地的距離
                                   else:  ##無法到達的地形
                                          print("無法抵達目的地")
                                          return False
                            else:  ##此軍隊已經移動過
                                   print("此軍隊已經移動過")
                                   return False
                            if (rang <= player.army[i].movement):  ##合法移動範圍
                                   for j in range(len(player2.army)):
                                          if (player2.army[j].x == x and player2.army[j].y == y):
                                                 print("與敵人重疊")
                                                 return False
                                   player.army[i].x = x  ##移動軍隊
                                   player.army[i].y = y
                                   player.army[i].moved = 1
                                   print("移動成功")
                                   return True
                            else:  ##非法移動範圍
                                   print("超出移動範圍")
                                   return False
                     else:  ##軍隊死亡
                            print("軍隊已死亡不能移動")
                            return False
              else:  ##無此軍隊
                     print("無此軍隊")
                     return False
       except:##軍隊尚未設定
              print("軍隊尚未set")
              return False