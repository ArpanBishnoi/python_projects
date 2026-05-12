import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()
def get_conn():
    return sqlite3.connect('app.db') 
conn = get_conn()
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY ,name TEXT, password TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT,user_id INTEGER)')
conn.commit()
conn.close()
class User(BaseModel):
    username: str
    password: str
class Task(BaseModel):
    task: str    
@app.post('/signup')
def signup(user : User):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name,password) VALUES(?,?)' , (user.username,user.password))
    conn.commit()
    conn.close()
    return{'MESSAGE':'user added'}   
@app.post('/login')
def login(user:User):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ? and password = ?',(user.username,user.password ))
    result = cursor.fetchone()
    conn.close()
    if result:
        return{'message': 'LOGIN SUCCESSFUL'}
    else:
        return{'message': 'Invalid login'} 
@app.post('/tasks/{user_id}')
def add_task(user_id: int,item: Task):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task,user_id) VALUES(?,?)',(item.task, user_id,))
    conn.commit()
    conn.close()
    return {'Message': 'Task added'}
@app.get('/tasks/{user_id}')
def get_tasks(user_id : int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE user_id = ?',(user_id,))
    rows = cursor.fetchall()
    conn.close()
    tasks = []
    for row in rows:
        tasks.append({
            'id': row[0],
            'task': row[1],
            'user_id': row[2]})
    return{'tasks': tasks}          