import requests
from bs4 import BeautifulSoup

search = input("Type what you are searching")

def searchWord(user_input):
    pass

#//Now finding the correct link to search\\
def getUrl(query):
        respons =   requests.get(
        "https://www.finn.no/bap/forsale/search.html?sort=RELEVANCE",
        params={"q": query})
        return getContent(respons.url)

#//Extract the content i want from search
def getContent(query_url):
    page = requests.get(query_url)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(class_="md:col-span-2")
    
    resultElements = result.find_all("article", class_="ads__unit")
    articleContent = result.find_all("div", class_="ads__unit__content")
    # pricing = result.find_all("div", class_="ads__unit__img__ratio__price")
    print(len(resultElements))
    for content in resultElements:
        title = content.find("h2", class_="ads__unit__content__title").text.strip()
        pricing = content.find("div", class_="ads__unit__img__ratio__price").text.strip()
        link = content.find_all("a")[0]["href"]
        print(f"{title}")
        print(f"{pricing}")
        print(f"{link}\n")
        print()

