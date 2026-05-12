from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
app = FastAPI()
def get_conn():
    return sqlite3.connect('ragbasics.db')
conn = get_conn()
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY, topic TEXT,  content TEXT)')
conn.commit()
class Notes(BaseModel):
    topic: str
    content : str
class Question(BaseModel):
    question : str    
@app.post('/add notes')
def add_notes(item:Notes):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (topic,content) VALUES(?,?)' , (item.topic,item.content))
    conn.commit()
    conn.close()
@app.post('/ask')
def ask(item:Question):
    if 'api' in item.question.lower():
         conn = get_conn()
         cursor = conn.cursor()
         cursor.execute('SELECT * FROM notes WHERE topic =?',(item.question,))
         result = cursor.fetchone()
         return {
         'retrieved_note': result
     }
         conn.commit()
         conn.close()
    
            

