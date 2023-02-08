import requests
from bs4 import BeautifulSoup

def write_to_file(date, title, company, location, url):
    file1 = open("scrapeContent.txt", "a")
    date_line = [f"{date}\n"]
    title_line = [f"{title}\n"]
    company_line = [f"{company}\n"]
    location_line = [f"{location}\n"]
    url_line = [f"{url}\n"]
    spacing_line = ["\n"]
    file1.writelines(date_line)
    file1.writelines(title_line)
    file1.writelines(company_line)
    file1.writelines(location_line)
    file1.writelines(url_line)
    file1.writelines(spacing_line)
    file1.close()


search = input(" What jobtitle are you searching for? ").lower()

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#Find everything in "ResultContainer" ID
result = soup.find(id="ResultsContainer")

#Finds all the <div> tags in the "card_content"
job_element = result.find_all("div", class_="card-content")

#Searches all the <h2> tags with lamda text str and convert everything to small letters
job_search = result.find_all(
"h2", string=lambda text: search in text.lower()
)

#Move up the hiarchy, going thru the <div class= "card-content" instead of only <h2> 
job_search_elements = [
    h2_element.parent.parent.parent for h2_element in job_search
]

#parsing through 
for job_element in job_search_elements:
    date_posted = job_element.find("p", class_="is-small")
    title_element = job_element.find("h2", class_="title")
    company_name = job_element.find("h3", class_="subtitle")
    location = job_element.find("p", class_="location")
    url_link = job_element.find_all("a")[1]["href"]

    content_date = date_posted.text.strip()
    content_title = title_element.text.strip()
    content_company = company_name.text.strip()
    content_location = location.text.strip()
    write_to_file(content_date, content_title, content_company, content_location, url_link)