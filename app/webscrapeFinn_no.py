import requests
import colorama
from bs4 import BeautifulSoup
import time

colorama.init(autoreset=True)

#//Search convert all the whitespaces with + to make the correct search
def searchWord(user_input):
    f = user_input.replace(" ", "+").lower()
    getUrl(f)

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
    #//Shows how many advert found and sleeps program for 3sec
    print("Found ", len(resultElements), " Adverts on current search")
    time.sleep(3)

    for content in resultElements:
        title = content.find("h2", class_="ads__unit__content__title").text.strip()
        pricing = content.find("div", class_="ads__unit__img__ratio__price").text.strip()
        link = content.find_all("a")[0]["href"]
        id = content.find_all("a")[0]["id"]
        print(colorama.Fore.RED + f"ID: {colorama.Fore.CYAN + id}")
        print(f"{title}")
        print(colorama.Fore.GREEN + f"{pricing}")
        print(f"{link}\n")
        print()

if __name__ == "__main__":
    search = input("Type what you are searching: ")
    searchWord(search)
