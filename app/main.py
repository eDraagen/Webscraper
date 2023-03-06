import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup
import time

#// TODO: In checIfExists function: If price == "Ønskes kjøpt", want to pass it so it doesnt get added to DB.
#// TODO: With request and beautifulso up, also get the content from the advert aswell.

resultArr = []
counter = 0
db_path = r"C:\Users\einar\Documents\GitHub\Webscraper\databases\pythonSqlite.db"
conn = sqlite3.connect(db_path)
curs = conn.cursor()

#//Create sqlite database connection
def createConnection(path = db_path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print("Database already exists")

#Checks sqliteDb if ID already exists or not. Return 0 if it doesnt, return 1 if already exists
def checkIfExist(idCheck = resultArr):
    for ele in idCheck:
        result = curs.execute("""SELECT EXISTS (SELECT 1 FROM Adverts
                            WHERE ID=?)""", (ele[0],)).fetchone()[0]
        print(result)
        if result == 0:
            print("Creating ID")
            writeData(ele[0], ele[1], ele[2], ele[3], ele[4])   
        else:
            print("ID already exists")

#Writes to sqliteDB
def writeData(Id, Title, Price, Html, Location, counter = counter):
    counter += 1
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    curs.execute("INSERT INTO Adverts VALUES (:Id, :Title, :Price, :Html,  :Location)", {"Id": Id, "Title": Title, "Price": Price, "Html": Html, "Location":Location})
    conn.commit()
    conn.close()

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
        id = content.find_all("a")[0]["id"]
        title = content.find("h2", class_="ads__unit__content__title")
        pricing = content.find("div", class_="ads__unit__img__ratio__price")
        link = content.find_all("a")[0]["href"]
        location = content.find("div", class_="ads__unit__content__details").contents[-1].text.strip()
        allArray = [id, title.text.strip(), pricing.text.strip(), link, location]
        resultArr.append(allArray)
    return resultArr

def main():
    search = input("Type what you are searching: ")
    searchWord(search)
    createConnection()
    checkIfExist()
    print(f"Added {counter} adverts to DB")

if __name__ == "__main__":
    main()