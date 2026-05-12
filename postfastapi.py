from fastapi import FastAPI
app = FastAPI()
@app.post('/add')
def add_item():
    return {"message":"item added"}
@app.get('/')
def index():
    return{'message':'Home page working'}
        
