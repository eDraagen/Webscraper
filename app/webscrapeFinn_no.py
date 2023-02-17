import requests
from bs4 import BeautifulSoup
import time

resultArr = []

#//Search convert all the whitespaces with + to make the correct search
def searchWord(user_input):
    conv_user_input = user_input.replace(" ", "+").lower()
    getUrl(conv_user_input)

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
    #//Shows how many advert found and sleeps program for 3sec
    print("Found ", len(resultElements), " Adverts on current search")
    time.sleep(3)
    #//Figure out how to append the result into array then import it to sqlite later
    for content in resultElements:
        #//Location not working 100% yet.
        # location = content.find("div", class_="ads__unit__content__details").text.strip()
        id = content.find_all("a")[0]["id"]
        title = content.find("h2", class_="ads__unit__content__title")
        pricing = content.find("div", class_="ads__unit__img__ratio__price")
        link = content.find_all("a")[0]["href"]
        allArray = [id, title.text.strip(), pricing.text.strip(), link]
        resultArr.append(allArray)
    return resultArr

# search = input("Type what you are searching: ")
# searchWord(search)

# print(resultArr)