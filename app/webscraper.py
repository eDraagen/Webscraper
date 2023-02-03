import requests
from bs4 import BeautifulSoup

#// Uncomment this later
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
#//Will change the var names for more general use, not only python
#parsing through 
for job_element in job_search_elements:
    date_posted = job_element.find("p", class_="is-small")
    title_element = job_element.find("h2", class_="title")
    company_name = job_element.find("h3", class_="subtitle")
    location = job_element.find("p", class_="location")
    url_link = job_element.find_all("a")[1]["href"]
    print(date_posted.text.strip())
    print(title_element.text.strip())
    print(company_name.text.strip())
    print(location.text.strip())
    print(f"Apply here: {url_link}\n")
    print()

