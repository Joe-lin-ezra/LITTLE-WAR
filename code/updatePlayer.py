import sqlite3


def winTimesUpdate(name):
    connection = sqlite3.connect('Gamedb.db')
    c = connection.cursor()
    c.execute('SELECT * FROM Player WHERE name="%s"' % name)
    row = c.fetchone()
    id = row[0]
    max = row[2]
    max += 1
    c.execute('INSERT INTO Player (Player_ID, Name, Win_times) VALUES (%d, "%s", %d)' % (id, name, max))
    connection.commit()
    connection.close()

# def main():
#     playerUpdate('Brian', 1)
#
# if __name__ == '__main__':
#     main()