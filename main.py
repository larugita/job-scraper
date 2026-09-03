import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Scraper API is running"}

@app.get("/jobs")
def get_jobs(keyword: str = None, location: str = None, limit: int = 10, sort: str = None):
    conn = sqlite3.connect("jobs.db")
    conn.row_factory = sqlite3.Row
    query = "SELECT * FROM jobs"
    params = []

    cursor = conn.cursor()
    if keyword:
        query += " WHERE title LIKE ?"
        params.append(f"%{keyword}%")
    if location:
        if keyword:
            query += " AND location LIKE ?"
        else:
            query += " WHERE location like ?"
        params.append(f"%{location}%")

    if sort == "newest":
        query += " ORDER BY date DESC"
    
    query += " LIMIT ?"
    params.append(limit)

    cursor.execute(query, params)

    jobs = cursor.fetchall()
    jobs = [dict(job) for job in jobs]

    conn.close()
    return jobs