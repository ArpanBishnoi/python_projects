print('running new code')
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
app = FastAPI()
def get_conn():
    return sqlite3.connect('Tasks.db',check_same_thread=False)
conn = get_conn()
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY,task TEXT)')
conn.commit()
class TASK(BaseModel):
    task: str
@app.post('/add item')
def add_tasks(item:TASK):
    cursor.execute('INSERT INTO tasks (task) VALUES(?)',(item.task,))
    conn.commit()
    return {'Task added'}
@app.get('/tasks')
def read_tasks():
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    tasks = []
    for row in rows:
        tasks.append({'id': row[0],
                     'task':row[1]
                     })
    return {'Tasks':tasks}
@app.delete('/delete-tasks')
def delete_tasks(task_id : int):
    cursor.execute('DELETE FROM tasks WHERE id = ?',(task_id))
    conn.commit()
    return{'message':'DELETED'}
@app.put('/UPDATE TASKS')
def update_tasks(task_id:int , item:TASK):
    cursor.execute('UPDATE tasks SET task = ? WHERE id = ?',(item.task, task_id))
    conn.commit()
    return {'message':'UPDATED'}
