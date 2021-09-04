import sqlite3
# --------------------------------------------------------SQLite--------------------------------------------------------
# --------------------------------------------------------SQLite--------------------------------------------------------

    def register(self, username):
        result = False
        db = self.db
        db.execute('select name from Player where Name="%s"' % username)
        if db.fetchone() is None:
            result = True
            db.execute('SELECT MAX(Player_ID) FROM Player')
            max = db.fetchone()[0]
            max += 1
            db.execute('INSERT INTO Player (Player_ID, Name, Win_times) VALUES (%d, "%s", %d)' % (max, username, 0))
        else:
            result = False
        conn.commit()
        return {'result': result}

    def login(self, username):
        result = False
        conn = Server.conn
        db = Server.db
        c = db.cursor()
        c.execute('select name from Player where Name="%s"' % username)
        if c.fetchone() is not None:
            result = True
        else:
            result = False
        return {'result': result}

    # get 3 max rank, and userself rank
    def selectRank(self, name):
        dic = dict()
        conn = Server.conn
        db = Server.db
        c = db.cursor()
        c.execute('SELECT MAX(Player_ID) FROM Player')
        amount = c.fetchone()[0]
        c.execute("SELECT * FROM Player ORDER BY Win_times DESC")
        for i in range(1, amount):
            row = c.fetchone()
            if row[1] == name:
                dic.update({str(4): [str(i), row[0], row[1], row[2]]})
            if i <= 3:
                dic.update({str(i): [str(i), row[0], row[1], row[2]]})
        return dic

    # get map information
    def selectMap(self, id,):
        # dictionary to return
        dic = dict()
        dic.update({'Id': id})
        # connection
        conn = Server.conn
        db = Server.db
        c = db.cursor()
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
        dic.update({'Player1_HQ': {'x': HQ[0], 'y': HQ[1]}})
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
        return dic

    # get deploy
    def selectDeploy(self, id):
        dic = dict()
        conn = Server.conn
        db = Server.db
        db.execute("SELECT Player1_Unit FROM Deploy WHERE ID = %s" % id)
        unit = db.fetchone()[0]
        unit = unit.split(')(')
        for i in range(len(unit)):
            unit[i] = unit[i].strip('()').split(',')
            for j in range(len(unit[i])):
                unit[i][j] = int(unit[i][j])
        counter = 0
        for i in range(len(unit)):
            for j in range(unit[i][1]):
                db.execute(
                    "SELECT Type, Movement, Range, Ammo, Fuel, Vision FROM Land_Unit WHERE ArmyID = %d" % unit[i][0])
                tmp = db.fetchone()
                dic.update({counter: {'type': tmp[0], 'movement': tmp[1], 'range': tmp[2], 'ammo': tmp[3],
                                      'fuel': tmp[4], 'vision': tmp[5]}})
                counter += 1
        return dic

    def winTimesUpdate(self, name):
        conn = Server.conn
        db = Server.db
        db.execute('SELECT * FROM Player WHERE name="%s"' % name)
        row = db.fetchone()
        id = row[0]
        max = row[2]
        max += 1
        db.execute('INSERT INTO Player (Player_ID, Name, Win_times) VALUES (%d, "%s", %d)' % (id, name, max))
        conn.commit()
# --------------------------------------------------------SQLite--------------------------------------------------------
# --------------------------------------------------------SQLite--------------------------------------------------------
