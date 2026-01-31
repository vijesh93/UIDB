from fastapi import FastAPI
from app.db import get_connection

app = FastAPI(title="Learning API")

@app.get("/api/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, email FROM users;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {"id": r[0], "name": r[1], "email": r[2]}
        for r in rows
    ]


@app.get("/")
def home():
    return {"message": "Welcome to the Learning API!"}  
