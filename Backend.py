import os
import bcrypt
from google import genai
from jose import jwt
from datetime import datetime,timedelta
gemini_client = genai.Client(api_key=os.getenv("Gemini_API_KEY"))
import uvicorn
from fastapi import FastAPI, HTTPException
import sqlite3
import chromadb
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
SECRET_KEY = 'super_secret_key_change_later'
ALGORITHM = 'HS256'
def create_access_token(user_id):
    expire = datetime.utcnow() + timedelta(days = 1)
    payload = {
        'sub': str(user_id),
        'exp': expire
    }
    token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm=ALGORITHM
    
   )
    return token

@app.get("/")
def home():
    return {"message": "API is running"}


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


conn = sqlite3.connect("Saas.db", check_same_thread=False)
cursor = conn.cursor()
conn.commit
client = chromadb.PersistentClient(path="chroma_db")
notes_collection = client.get_or_create_collection(name="NOTEs")
memory_collection = client.get_or_create_collection(name="MEMOORY")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,email TEXT,password TEXT)"
)
conn.commit()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Notes(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER ,content TEXT)"
)
conn.commit()


def add_users(username, email, password):
    cursor.execute(
        "INSERT INTO Users(username,email,password) VALUES(?,?,?)",
        (username, email, password)
    )
    conn.commit()


def login_users(username, email, password):
    cursor.execute(
        "SELECT * FROM Users WHERE username = ? AND email = ?",
        (username, email)
    )
    user = cursor.fetchone()
    if user and verify_password(password, user[3]):
        return user
    else:
        return None


def add_notes(user_id, content):
    cursor.execute("INSERT INTO Notes(user_id,content) VALUES(?,?)", (user_id, content))
    conn.commit()
    note_id = cursor.lastrowid
    notes_collection.add(
        documents=[content], ids=[str(note_id)], metadatas=[{"user_id": user_id}]
    )


def get_notes(user_id):
    cursor.execute("SELECT * FROM Notes WHERE user_id = ?", (user_id,))
    return cursor.fetchall()


def search_notes(user_id, question):
    results = notes_collection.query(
        query_texts=[question], where={"user_id": user_id}, n_results=2
    )
    return results["documents"][0]


def generate_answer(prompt):
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text


def ask_ai(user_id, question):
    retrieved_notes = search_notes(user_id, question)
    if not retrieved_notes:
        raise HTTPException(status_code=404, detail="No notes found for this user")
    retrieved_memory = search_memory(user_id, question)
    notes_context = "\n".join(retrieved_notes)
    if retrieved_memory:
        memory_context = "\n".join(retrieved_memory)
    else:
        memory_context = ""
    prompt = f"""
    You are a helpful AI assistant.
    use the user's notes and memory to answer the question.
    Notes:
    {notes_context}
    Memory:
    {memory_context}
    Notes context:
    {notes_context}
    Question: {question}
    Give a helpful answer based only on provided context.
    """
    answer = generate_answer(prompt)
    memory_text = f"""
     Question:
    {question}
     Answer:
    {answer}
     """
    memory_collection.add(
        documents=[memory_text],
        ids=[str(cursor.lastrowid)],
        metadatas=[{"user_id": user_id}],
    )
    return answer


def search_memory(user_id, question):
    results = memory_collection.query(
        query_texts=[question], where={"user_id": user_id}, n_results=2
    )
    return results["documents"][0]


class NOTEINPUT(BaseModel):
    user_id: int
    content: str


class QuestionInput(BaseModel):
    user_id: int
    question: str


class UPDATENOTEINPUT(BaseModel):
    id: int
    content: str


class USERINPUT(BaseModel):
    username: str
    email: str
    password: str


class LOGINUSER(BaseModel):
    username: str
    email: str
    password: str


@app.post("/Register")
def create_user(item: USERINPUT):
    try:
        print("REGISTER POINT HIT")
        print(item)
        hashed_password = hash_password(item.password)
        add_users(item.username, item.email, hashed_password)
        return {"message": "User added successfully!!!"}
    except Exception as e:
        print("register error", e)
        return {"error": str(e)}


@app.post("/login")
def login(item: LOGINUSER):
    user = login_users(item.username, item.email, item.password)
    if user:
        token = create_access_token([0])
        return {"message": "logined susccessfully",'user_id': user[0], "token": token}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/notes")
def creat_note(item: NOTEINPUT):
    try:
        print("ENDPOINT REACHED")
        print(item)
        add_notes(item.user_id, item.content)
        return {"message": "Note Added !!!"}
    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}


@app.post("/ask")
def ask(item: QuestionInput):
    response = ask_ai(item.user_id, item.question)
    return {"response": response}


@app.get("/read_notes")
def read_notes(user_id: int):
    notes = get_notes(user_id)
    if not notes:
        raise HTTPException(status_code=404, detail="Notes not found")
    return {"notes": notes}


@app.put("/update notes")
def update_notes(item: UPDATENOTEINPUT):
    cursor.execute("UPDATE Notes SET content = ? WHERE id = ?", (item.content, item.id))
    conn.commit()
    return {"message": "Note Updated !!!"}


@app.delete("/Delete notes")
def delete_notes(delete_id: int):
    cursor.execute(
        "Delete FROM Notes WHERE id = ?", (delete_id,)
    )  # rememeber that we use i in place of user_id cause id increases but with use_id =1 we can have thousands of users so all will be deleted as id keep increasing but user_id can be shared by many users
    conn.commit()
    return {"message": "Note Deleted !!!"}
cursor.execute('SELECT username,password FROM Users')
print(cursor.fetchall())
