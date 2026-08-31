import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Scraper API is running"}

@app.get("/jobs")
def get_jobs(keyword: str = None, location: str = None):
    conn = sqlite3.connect("jobs.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    if keyword and location:
        cursor.execute("SELECT * FROM jobs WHERE title LIKE ? AND location LIKE ?", 
        (f"%{keyword}%", f"%{location}%"))
    elif keyword:
        cursor.execute("SELECT * FROM jobs WHERE title LIKE ?", (f"%{keyword}%",))
    elif location:
        cursor.execute("SELECT * FROM jobs WHERE location LIKE ?", (f"%{location}%",))
    else:
        cursor.execute("SELECT * FROM jobs")

    jobs = cursor.fetchall()
    jobs = [dict(job) for job in jobs]

    conn.close()
    return jobs