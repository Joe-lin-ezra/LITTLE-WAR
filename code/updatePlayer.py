import sqlite3


def winTimesUpdate(name):
    connection = sqlite3.connect('Gamedb.db')
    c = connection.cursor()
    c.execute('SELECT * FROM Player WHERE name="%s"' % name)
    row = c.fetchone()
    max = row[2]
    max += 1
    c.execute('UPDATE Player SET Win_times = "%d" WHERE name="%s"' % (max, name))
    connection.commit()
    connection.close()

# def main():
#     playerUpdate('Brian', 1)
#
# if __name__ == '__main__':
#     main()