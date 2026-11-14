from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db, init_db

init_db()

class UserCreate(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/users")
def get_users():
    conn = get_db()
    rows = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    result = []
    for row in rows:
        result.append(dict(row))
    return result
    

@app.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_db()
    row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return dict(row) 

@app.post("/users")
def create_user(user: UserCreate):
    conn = get_db()
    cursor = conn.execute("INSERT INTO users (name, age) VALUES (?,?)", (user.name, user.age))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, "name": user.name, "age": user.age}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_db()
    cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Не удалось удалить пользователя")
    return {"message": "Пользователь удален"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    conn = get_db()
    cursor = conn.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (user.name, user.age, user_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    if updated == 0:
        raise HTTPException(status_code=404, detail="Не удалось обновить пользователя")
    return {"id": user_id, "name": user.name, "age": user.age}