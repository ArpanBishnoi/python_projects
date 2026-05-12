from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
tasks = []
task_id_counter = 1
class Task(BaseModel):
    task: str
@app.post('/Add Tasks')
def add_tasks(item:Task):
    global task_id_counter
    new_task = {'id': task_id_counter,'task':item.task}
    tasks.append(new_task)
    task_id_counter += 1
    return {'Message': 'Task added','task': new_task}
@app.get('/Tasks')    
def read_tasks():
    return{'Tasks':tasks}
@app.delete('/Delete tasks')
def delete_tasks(task_id : int):
    for task in tasks :
        if task['id'] == task_id:
            tasks.remove(task)
            return{'Message':'Deleted','Task':task}
    else:
         return('task not found')
@app.put('/update tasks')
def update_tasks(task_id:int , item:Task):
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = item.task
            return{'message':'Updated','Task':task}
    else:
            return{'Invalid input'}





                  
























