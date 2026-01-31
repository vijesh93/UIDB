from email.mime import text
from fastapi import FastAPI, Depends
from app.db import get_connection
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text


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


@app.get("/api/users_sqlalchemy")
def get_users(db: Session = Depends(get_db)): # FastAPI calls get_db()
    
    # Wrap the string in text()
    query = text("SELECT id, name, email FROM users;")
    result = db.execute(query)
    
    rows = result.fetchall()

    return [
        {"id": r[0], "name": r[1], "email": r[2]}
        for r in rows
    ]


@app.get("/")
def home():
    return {"message": "Welcome to the Learning API!"}  
