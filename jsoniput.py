from fastapi import FastAPI
from pydantic import BaseModel
class Task(BaseModel):
    task : str
app = FastAPI()
@app.get('/') 
def index():
    return{'message' :'This is home page'} 
@app.post('/add')
def add_item(item: Task):
    return{'message':'Task added','Task':item.task}
    
           