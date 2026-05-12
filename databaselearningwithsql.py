import sqlite3
conn = sqlite3.connect('Tasks.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,task TEXT)')
cursor.execute('INSERT INTO tasks(task) VALUES(?)',('Learn Python',))
conn.commit()
cursor.execute('SELECT * FROM tasks')
rows = cursor.fetchall()
print(rows)
conn.close
