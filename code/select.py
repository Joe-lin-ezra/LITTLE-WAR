import sqlite3
import json


# get 3 max rank, and userself rank
def selectRank(id):
    dic = dict()
    connection = sqlite3.connect("Gamedb.db")
    c = connection.cursor()
    c.execute("SELECT * FROM Player ORDER BY Win_times DESC")
    for i in range(3):
        j = c.fetchone()
        dic.update({j[0]: {j[1]: j[2]}})
    c.execute("SELECT * FROM Player WHERE Player_ID = %d" % id)
    tmp = c.fetchone()
    dic.update({tmp[0]: {tmp[1]: tmp[2]}})
    return json.dumps(dic)


#
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
    size = size.strip('()')
    size = size.split(',')
    for i in range(len(size)):
        size[i] = int(size[i])
    dic.update({'x': size[0], 'y': size[1]})
    del size
    # get Player1 HQ
    c.execute("SELECT Player1_HQ FROM Map WHERE Map_ID = %s" % id)
    HQ = c.fetchone()[0]
    HQ = HQ.strip('()')
    HQ = HQ.split(',')
    for i in range(len(HQ)):
        HQ[i] = int(HQ[i])
    dic.update({'Player1_HQ': {'x': HQ[0],'y': HQ[1]}})
    del HQ
    # get Player2 HQ
    c.execute("SELECT Player2_HQ FROM Map WHERE Map_ID = %s" % id)
    HQ = c.fetchone()[0]
    HQ = HQ.strip('()')
    HQ = HQ.split(',')
    for i in range(len(HQ)):
        HQ[i] = int(HQ[i])
    dic.update({'Player2_HQ': {'x': HQ[0], 'y': HQ[1]}})
    # get Player1 Area
    c.execute("SELECT Player1_Area FROM Map WHERE Map_ID = %s" % id)
    area = c.fetchone()[0]
    area = area.split(')(')
    for i in range(len(area)):
        area[i] = area[i].strip('()')
        area[i] = area[i].split(',')
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
        area[i] = area[i].strip('()')
        area[i] = area[i].split(',')
    for i in range(len(area)):
        for j in range(len(area[i])):
            area[i][j] = int(area[i][j])
    dic.update({'Player2_Area': {'x1': area[0][0], 'y1': area[0][1], 'x2': area[1][0], 'y2': area[1][1]}})
    del area
    c.execute("SELECT Water FROM Map WHERE Map_ID = %s" % id)
    for i, j in dic.items():
        print(i, ':', j)

def main():
    selectMap(1)



if __name__ == '__main__':
    main();