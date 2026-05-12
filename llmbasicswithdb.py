from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
app = FastAPI()
def get_conn():
    return sqlite3.connect('AI_TASK MANAGER.db')
conn = get_conn()
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT ,ai_suggestion TEXT) ')
conn.commit()
class Tasks(BaseModel):
    task : str
@app.post('/add tasks')
def ai_taskbreaker(item:Tasks):
    if 'learn' in item.task.lower():
        ai_suggestion = ('BREAK THE TASK INTO SMALL STEPS')
    else:
        ai_suggestion = ('WORK consistently')    
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, ai_suggestion) VALUES(?,?)' ,(item.task,ai_suggestion))
    conn.commit()
    conn.close()
    return{'id' : cursor.lastrowid, 
            'Task': item.task ,
          'Message':'task added' ,
          'ai_suggestion': ai_suggestion}



