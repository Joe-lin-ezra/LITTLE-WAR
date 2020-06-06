import json
from Player import Player
from Army import Army
from Headquarter import Headquarter

def constructPlayer(datas):
    datas = json.loads(datas)
    # datas = eval(datas) ##將str轉化成dict by Dan
    # print(type(datas))
    # print(datas['0'])
    player1 = Player()
    for i in range(len(datas)):
        index = str(i)
        player1.army.append(Army(type=datas[index]['type'],
                                 hp=100,
                                 movement=datas[index]['movement'],
                                 ammo = datas[index]['ammo'],
                                 fuel = datas[index]['fuel'],
                                 atk=50,
                                 atkRange=datas[index]['range'],
                                 vision=datas[index]['vision'],
                                 x=None,
                                 y=None))
        # ** search datas and give hq (x,y)
        # Player.hq = Headquarter(hp=20, x=0, y=0)##我隨便打數字喔，因為跑不動 by DannisMa
    return player1 ##需要return player 才能正確建構player在主程式by Dan


def constructMap(datas):
    map = list()
    for i in range(datas['sizeX']):
        map.append([])
        for j in range(datas['sizeY']):
            map[i].append(0)

    water = datas['water']
    for i in range(len(water)):
        map[ water[i][0]-1 ][ water[i][1]-1 ] = 1

    mountain = datas['mountain']
    for i in range(len(mountain)):
        map[ mountain[i][0]-1 ][ mountain[i][1]-1 ] = 2
    return map
