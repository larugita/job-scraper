import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Scraper API is running"}

@app.get("/jobs")
def get_jobs():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    conn.close()
    return jobs