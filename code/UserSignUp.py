import sqlite3

def register(username):
    success = False
    connection = sqlite3.connect('gamedb.db')
    c = connection.cursor()
    c.execute('select name from Player where Name="%s"' % username)
    if c.fetchone() is None:
        success = True
        c.execute('SELECT MAX(Player_ID) FROM Player')
        max = c.fetchone()[0]
        max += 1
        c.execute('INSERT INTO Player (Player_ID, Name, Win_times) VALUES (%d, "%s", %d)' % (max, username, 0))
    else:
        success = False
    connection.commit()
    connection.close()
    return success

def login(username):
    success = False
    connection = sqlite3.connect('gamedb.db')
    c = connection.cursor()
    c.execute('select name from Player where Name="%s"' % username)
    if c.fetchone() is not None:
        success = True
    else:
        success = False
    connection.close()
    return success