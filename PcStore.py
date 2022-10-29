import sqlite3
db = sqlite3.connect('PcStore.db')
cur = db.cursor()

file = open('PC_magazine.sql')
content = file.read()
file.close()
cur.executescript(content)
db.commit()