from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
tasks = []
class Task(BaseModel):
    task:str
@app.get('/')
def homepage():
    return{'message':'HELLO THERE!'}
@app.post('/add')
def add_item(item:Task):
     tasks.append(item.task)
     return{'Task added'}
@app.get('/Tasks')
def read_tasks():
    return{'tasks':tasks}    
@app.delete('/delete/{index}')
def delete_tasks(index:int):
    if index<len(tasks):
        removed = tasks.pop(index)
        return{' message':'Task deleted',
        'TASK':removed}
    else:
        return{'Invalid command'}
@app.put('/update/{index}')
def update_task(index: int, item:Task):
    if index < len(tasks):
        tasks[index] = item.task
        return {'message':'Updated'}
    else:
        return {'error': 'Invalid index'}
 



