import requests
import csv
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

soup = fetch_page("https://realpython.github.io/fake-jobs/")

def scrape_jobs(soup):
    jobs = soup.find_all("div", class_="card")
    jobs_data = []
    for job in jobs:
        title = job.find("h2", class_="title")
        company = job.find("h3", class_ = "company")
        location = job.find("p", class_ = "location")
        apply_link = job.find("a", string="Apply")
        link = apply_link["href"]
        job_dict = {
            "title": title.text.strip(),
            "company": company.text.strip(),
            "location": location.text.strip(),
            "link": link
        }
        jobs_data.append(job_dict)

    return jobs_data

jobs_data = scrape_jobs(soup)

def filter_jobs(jobs_data, keyword):
    filtered_jobs = []
    for job in jobs_data:
        if keyword.lower() in job["title"].lower():
            filtered_jobs.append(job)
    return filtered_jobs

filtered_jobs = filter_jobs(jobs_data, "python")

if filtered_jobs:
    with open("python_jobs.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = filtered_jobs[0].keys())
        writer.writeheader()
        writer.writerows(filtered_jobs)