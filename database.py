import sqlite3


def drop_table():
    with sqlite3.connect('volumes.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS volumes;""")
    return True


def create_db():
    with sqlite3.connect('volumes.db') as connection:
        c = connection.cursor()
        table = '''CREATE TABLE  volumes(
        id INTEGER PRIMARY KEY,
        DATETIME DEFAULT (STRFTIME('%d-%m-%Y   %H:%M', 'NOW','localtime')),
		name TEXT NOT NULL,
		mountpoint TEXT NOT NULL,
		size INTEGER)'''
        c.execute(table)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
