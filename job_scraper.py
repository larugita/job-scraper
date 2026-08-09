import requests
import csv
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

soup = fetch_page("https://realpython.github.io/fake-jobs/")

jobs = soup.find_all("div", class_="card")

jobs_data = []

for job in jobs:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_ = "company")
    apply_link = job.find("a", string="Apply")
    link = apply_link["href"]
    job_dict = {
        "title": title.text.strip(),
        "company": company.text.strip(),
        "link": link
    }
    jobs_data.append(job_dict)

python_jobs = []

for job in jobs_data:
    if "python" in job["title"].lower():
        python_jobs.append(job)

if python_jobs:
    with open("python_jobs.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = python_jobs[0].keys())
        writer.writeheader()
        writer.writerows(python_jobs)
