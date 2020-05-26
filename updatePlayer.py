import sqlite3


def playerUpdate(name, winTimes):
    connection = sqlite3.connect('gamedb.db')
    c = connection.cursor()
    c.execute('SELECT MAX(Player_ID) FROM Player')
    max = c.fetchone()[0]
    if None == max:
        c.execute('INSERT INTO Player (Player_ID, Name, Win_times) VALUES (1, "%s", %d)' % (name, winTimes))
    else:
        max += 1
        c.execute('INSERT INTO Player (Player_ID, Name, Win_times) VALUES (%d, "%s", %d)' % (max, name, winTimes))
    connection.commit()
    connection.close()

def main():
    playerUpdate('Brian', 1)

if __name__ == '__main__':
    main()