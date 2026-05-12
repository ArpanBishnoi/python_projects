from fastapi import FastAPI
app = FastAPI()
@app.post('/')
def index():
    return{'message':'Hello world'}