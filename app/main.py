from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db():
conn = psycopg2.connect(DATABASE_URL)
return conn

class Task(BaseModel):
title: str
description: str

@app.get("/")
def root():
return {"message": "Task Manager API running!"}

@app.post("/tasks")
def create_task(task: Task):
conn = get_db()
cur = conn.cursor()
cur.execute(
"INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING id",
(task.title, task.description),
)
new_id = cur.fetchone()[0]
conn.commit()
cur.close()
conn.close()
return {"id": new_id, "task": task}

