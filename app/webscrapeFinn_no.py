import requests
from bs4 import BeautifulSoup

#URL: Finn.no / Torget / Sport og friluftliv / Fulldemper / Møre og Romsdal
url = "https://www.finn.no/bap/forsale/search.html?bikes_type=5&category=0.69&gsq=sykkel%3A3f6d22d9bbab&location=0.20015&sort=RELEVANCE"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#Somewhat working but very messy
result = soup.find(class_="md:col-span-2")
search = result.find_all("article", class_="ads__unit")


#This finds the pricing for all content
pricing = result.find_all("div", class_="ads__unit__img__ratio__price")
priceList = []
for price in pricing:
    print(price.text.strip())


#// Find a smarter way to sort stuff out and to find the stuff more genereal instead of fuckton of spaghetti code\\ anus
#Do something like take search var, add a for loop to itterate through, and add spesific vars to pick out content i want