import sqlite3
from sqlite3 import Error


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

#This works, Return 0 if ID does NOT exists, and 1 if exists
def checkIfExist(ID):
    result = curs.execute("""SELECT EXISTS (SELECT 1 FROM Adverts
                            WHERE ID=?)""", (ID,)).fetchone()[0]
    if result == 0:
        print(ID)
    else:
        print("ID Already Exists")

#Dummy function, just for testing
def readData():
    curs.execute("SELECT * FROM Adverts")
    print(curs.fetchall())

#Writes to sqliteDB
def writeData(Id, Title, Price, Html):
    curs.execute("INSERT INTO Adverts VALUES (:Id, :Title, :Price, :Html)", {"Id": Id, "Title": Title, "Price": Price, "Html": Html})
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # createConnection(db_path)
    # readData()
    # writeData(54321, "This is a test title", 35000, "thisMustBeDeleted.com")
    checkIfExist(2534523534)