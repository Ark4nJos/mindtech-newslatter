import sqlite3

db = sqlite3.connect('database.db')

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS email (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL UNIQUE)")


if __name__ == '__main__':
    cursor.execute("INSERT INTO email VALUES(1, 'rodrigo@email.com')")
    db.commit()
    cursor.execute('SELECT * FROM email')
    print(cursor.fetchall())
    db.close()