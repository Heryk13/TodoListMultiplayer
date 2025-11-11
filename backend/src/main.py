from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.get("/db-check")
def db_check():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        dbname=os.getenv("POSTGRES_DB", "appdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "password"),
    )
    with conn.cursor() as cur:
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
    conn.close()
    return {"db_time": result[0]}
