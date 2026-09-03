import requests
import sqlite3

# Connect to the SQLite database

connection = sqlite3.connect("jobs.db")

# Create a cursor to send SQL commands to the database

cursor = connection.cursor()

# Create the jobs table

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
id INTEGER PRIMARY KEY,
title TEXT,
company TEXT,
location TEXT,
date TEXT,
link TEXT UNIQUE
)
""")

# Save the database changes

connection.commit()


def fetch_jobs(url):

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None


data = fetch_jobs("https://boards-api.greenhouse.io/v1/boards/stripe/jobs")

jobs_data = []

if data:

    for job in data["jobs"]:

        job_dict = {
            "title": job["title"],
            "company": job["company_name"],
            "location": job["location"]["name"],
            "date": job["first_published"],
            "link": job["absolute_url"]
        }

        jobs_data.append(job_dict)


for job in jobs_data:

    cursor.execute("""
    INSERT OR IGNORE INTO jobs (title, company, location, date, link)
    VALUES(?, ?, ?, ?, ?)
    """, (
        job["title"],
        job["company"],
        job["location"],
        job["date"],
        job["link"]
    ))

# Save inserted jobs

connection.commit()


cursor.execute("SELECT COUNT(*) FROM jobs")

count = cursor.fetchone()[0]

print("Total jobs:", count)

# Close the database connection when finished

connection.close()