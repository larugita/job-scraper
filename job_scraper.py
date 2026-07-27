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
    print(title.text)
