import requests
from bs4 import BeautifulSoup

#// Uncomment this later
#search = input(" What jobtitle are you searching for? ").lower()

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id="ResultsContainer")
job_element = result.find_all("div", class_="card-content")


python_job = result.find_all(
"h2", string=lambda text: "python" in text.lower()
)

print(python_job)


# for job_element in python_job:
#     date_posted = job_element.find("p", class_="is-small")
#     title_element = job_element.find("h2", class_="title")
#     company_name = job_element.find("h3", class_="subtitle")
#     location = job_element.find("p", class_="location")

#     print(date_posted.text.strip())
#     print(title_element.text.strip())
#     print(company_name.text.strip())
#     print(location.text.strip())
#     print()

