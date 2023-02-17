import sqlite3
from sqlite3 import Error
import webscrapeFinn_no


db_path = r"C:\Users\einar\Documents\GitHub\Webscraper\databases\pythonSqlite.db"
conn = sqlite3.connect(db_path)
curs = conn.cursor()

#//Create sqlite database connection
def createConnection(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print()

#Checks sqliteDb if ID already exists or not. Return 0 if it doesnt, return 1 if already exists
def checkIfExist(ID):
    result = curs.execute("""SELECT EXISTS (SELECT 1 FROM Adverts
                            WHERE ID=?)""", (ID,)).fetchone()[0]
    if result == 0:
        print(ID)
    else:
        print("ID Already Exists")

#Writes to sqliteDB
def writeData(Id, Title, Price, Html):
    curs.execute("INSERT INTO Adverts VALUES (:Id, :Title, :Price, :Html)", {"Id": Id, "Title": Title, "Price": Price, "Html": Html})
    conn.commit()
    conn.close()

def main():
    createConnection(db_path)
    

if __name__ == "__main__":
    main()