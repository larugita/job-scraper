import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Scraper API is running"}

@app.get("/jobs")
def get_jobs(keyword: str = None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    if keyword:
        cursor.execute("SELECT * FROM jobs WHERE title LIKE ?", (f"%{keyword}%",))
    else:
        cursor.execute("SELECT * FROM jobs")

    jobs = cursor.fetchall()

    conn.close()
    return jobs