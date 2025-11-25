from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {}

class User(BaseModel):
    username: str
    password: str

@app.post("/signup")
def signup(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    users[user.username] = user.password
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: User):
    if users.get(user.username) == user.password:
        return {"message": f"Welcome {user.username}!"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
