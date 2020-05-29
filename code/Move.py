import Player
import Army
import select
import cmath
import math

def countRange(armyX,armyY,distanceX,distanceY):
       range = cmath.sqrt((armyX - distanceX) * (armyX - distanceX) + (armyY - distanceY * armyY - distanceY))
       range = math.ceil(range.real)
       return range

def move(player = Player(),i,x,y):## x y 是要過去的座標
       if (1<= player.army[i].type <=10):##合法兵種
              range = countRange(player.army[i].x, player.army[i].y, x, y)
       else:##錯誤軍種
              return False
       if(range<=player.army[i].movement):##合法移動範圍
              player.army[i].x = x ##移動軍隊
              player.army[i].y = y
              return True
       else:##非法移動範圍
              return False