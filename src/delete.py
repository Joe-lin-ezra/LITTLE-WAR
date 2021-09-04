import sqlite3

def deletePlayer(id=0, name=''):
    connection = sqlite3.connect('gamedb.db')
    c = connection.cursor()
    c.execute('DELETE FROM PLAYER WHERE Player_ID = 4')
    c.execute('DELETE FROM PLAYER WHERE Player_ID = 5')

    connection.commit()
    connection.close()

def main():
    deletePlayer(12)

if __name__ == '__main__':
    main()