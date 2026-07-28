import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

jobs = soup.find_all("div", class_="card")
print(len(jobs))

for job in jobs:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_ = "company")
    apply_link = job.find("a", string="Apply")
    url = apply_link["href"]
    print(title.text + " — " + company.text + " : " + url)

