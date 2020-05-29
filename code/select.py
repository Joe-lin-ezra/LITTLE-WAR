import sqlite3
import json
from Player import Player
from Army import Army
from Headquarter import Headquarter


# get 3 max rank, and userself rank
def selectRank(id):
    dic = dict()
    connection = sqlite3.connect("Gamedb.db")
    c = connection.cursor()
    c.execute("SELECT * FROM Player ORDER BY Win_times DESC")
    for i in range(1, 4):
        row = c.fetchone()
        dic.update({i: [row[0], row[1], row[2]]})
    c.execute("SELECT * FROM Player WHERE Player_ID = %d" % id)
    row = c.fetchone()
    dic.update({"4": [row[0], row[1], row[2]]})
    return json.dumps(dic)


# get map information
def selectMap(id):
    # dictionary to return
    dic = dict()
    dic.update({'Id': id})
    # connection
    connection = sqlite3.connect("Gamedb.db")
    c = connection.cursor()
    # get map size
    c.execute("SELECT T_size FROM Map WHERE Map_ID = %s" % id)
    size = c.fetchone()[0]
    size = size.strip('()').split(',')
    for i in range(len(size)):
        size[i] = int(size[i])
    dic.update({'sizeX': size[0], 'sizeY': size[1]})
    del size
    # get Player1 HQ
    c.execute("SELECT Player1_HQ FROM Map WHERE Map_ID = %s" % id)
    HQ = c.fetchone()[0]
    HQ = HQ.strip('()').split(',')
    for i in range(len(HQ)):
        HQ[i] = int(HQ[i])
    dic.update({'Player1_HQ': {'x': HQ[0],'y': HQ[1]}})
    del HQ
    # get Player2 HQ
    c.execute("SELECT Player2_HQ FROM Map WHERE Map_ID = %s" % id)
    HQ = c.fetchone()[0]
    HQ = HQ.strip('()').split(',')
    for i in range(len(HQ)):
        HQ[i] = int(HQ[i])
    dic.update({'Player2_HQ': {'x': HQ[0], 'y': HQ[1]}})
    # get Player1 Area
    c.execute("SELECT Player1_Area FROM Map WHERE Map_ID = %s" % id)
    area = c.fetchone()[0]
    area = area.split(')(')
    for i in range(len(area)):
        area[i] = area[i].strip('()').split(',')
    for i in range(len(area)):
        for j in range(len(area[i])):
            area[i][j] = int(area[i][j])
    dic.update({'Player1_Area': {'x1': area[0][0], 'y1': area[0][1], 'x2': area[1][0], 'y2': area[1][1]}})
    del area
    # get Player2 Area
    c.execute("SELECT Player2_Area FROM Map WHERE Map_ID = %s" % id)
    area = c.fetchone()[0]
    area = area.split(')(')
    for i in range(len(area)):
        area[i] = area[i].strip('()').split(',')
    for i in range(len(area)):
        for j in range(len(area[i])):
            area[i][j] = int(area[i][j])
    dic.update({'Player2_Area': {'x1': area[0][0], 'y1': area[0][1], 'x2': area[1][0], 'y2': area[1][1]}})
    del area
    # get water coordinate
    c.execute("SELECT Water FROM Map WHERE Map_ID = %s" % id)
    water = c.fetchone()[0]
    water = water.split(')(')
    for i in range(len(water)):
        water[i] = water[i].strip(')(').split(',')
        for j in range(len(water[i])):
            water[i][j] = int(water[i][j])
    dic.update({'water': water})
    del water
    # get mountain coordinate
    c.execute("SELECT Mountain FROM Map WHERE Map_ID = %s" % id)
    mountain = c.fetchone()[0]
    mountain = mountain.split(')(')
    for i in range(len(mountain)):
        mountain[i] = mountain[i].strip(')(').split(',')
        for j in range(len(mountain[i])):
            mountain[i][j] = int(mountain[i][j])
    dic.update({'mountain': mountain})
    del mountain

    # for i, j in dic.items():
    #     print(i, ':', j)

    return json.dumps(dic)


# get deploy
def selectDeploy(id):
    dic = dict()
    connection = sqlite3.connect("Gamedb.db")
    c = connection.cursor()

    c.execute("SELECT Player1_Unit FROM Deploy WHERE ID = %s" % id)
    unit = c.fetchone()[0]
    unit = unit.split(')(')
    for i in range(len(unit)):
        unit[i] = unit[i].strip('()').split(',')
        for j in range(len(unit[i])):
            unit[i][j] = int(unit[i][j])
    counter = 0
    for i in range(len(unit)):
        for j in range(unit[i][1]):
            c.execute("SELECT Type, Movement, Range, Ammo, Fuel, Vision FROM Land_Unit WHERE ArmyID = %d" % unit[i][0])
            tmp = c.fetchone()
            dic.update({counter: {'type': tmp[0], 'movement': tmp[1], 'range': tmp[2], 'ammo': tmp[3],
                        'fuel': tmp[4], 'vision': tmp[5]}})
            counter += 1

    return json.dumps(dic)
    # print(tmp, len(tmp))
    # for j in range(unit[i][1]):
    #     army = Army(type=tmp[0], hp=20, atk=None, atkRange=tmp[2], vision=tmp[5],x=None, y=None)
    #     player1.army.append(army)

    # for i in range(len(player1.army)):
    #     print(player1.army[i].type, player1.army[i].hp, player1.army[i].atk,
    #     player1.army[i].atkRange, player1.army[i].vision, player1.army[i].x, player1.army[i].y)

def constructPlayer(datas):
    datas = json.loads(datas)
    # print(datas['0'])
    player1 = Player()
    for i in range(len(datas)):
        index = str(i)
        player1.army.append(Army(type=datas[index]['type'],
                                 hp=10,
                                 movement=datas[index]['movement'],
                                 atk=1,
                                 atkRange=datas[index]['range'],
                                 vision=datas[index]['vision'],
                                 x=None,
                                 y=None))
        # ** search datas and give hq (x,y)
        Player.hq = Headquarter(hp=20, x=, y=)



def constructMap(datas):
    datas = json.loads(datas)
    global map
    map = list()
    for i in range(datas['sizeX']):
        map.append([])
        for j in range(datas['sizeY']):
            map[i].append(0)

    water = datas['water']
    for i in range(len(water)):
        map[ water[i][0] ][ water[i][1] ] = 1

    mountain = datas['mountain']
    for i in range(len(mountain)):
        map[ mountain[i][0] ][ mountain[i][1] ] = 2


def main():
    # print(selectRank(1))
    # map = selectMap(1)
    # map = json.loads(map)
    # for i, j in map.items():
    #     print(i, ':', j)
    constructPlayer(selectDeploy(1))
    # constructMap(selectMap(1))
    pass


if __name__ == '__main__':
    main()