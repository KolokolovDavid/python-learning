from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int

app = FastAPI()

users = {
    1: {"name": "David", "age": 17},
    2: {"name": "Anna", "age": 16},
    3: {"name": "Boris", "age": 20}
}

@app.get("/users")
def get_users():
    return users

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return users[user_id]

@app.post("/users")
def create_user(user: UserCreate):
    new_id = max(users) + 1
    users[new_id] = {"name": user.name, "age": user.age}
    return {"id": new_id, "name": user.name, "age": user.age}

@app.delete("/users")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    del users[user_id]
    return {"message": "Пользователь удален"}