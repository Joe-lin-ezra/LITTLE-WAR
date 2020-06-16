import sqlite3

def register(username):
    result = False
    connection = sqlite3.connect('Gamedb.db')
    c = connection.cursor()
    c.execute('select name from Player where Name="%s"' % username)
    if c.fetchone() is None:
        result = True
        c.execute('SELECT MAX(Player_ID) FROM Player')
        max = c.fetchone()[0]
        max += 1
        c.execute('INSERT INTO Player (Player_ID, Name, Win_times) VALUES (%d, "%s", %d)' % (max, username, 0))
    else:
        result = False
    connection.commit()
    connection.close()
    return {'result': result}

def login(username):
    result = False
    connection = sqlite3.connect('gamedb.db')
    c = connection.cursor()
    c.execute('select name from Player where Name="%s"' % username)
    if c.fetchone() is not None:
        result = True
    else:
        result = False
    connection.close()
    return {'result': result}
