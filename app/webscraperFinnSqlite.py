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

def readData():
    curs.execute("SELECT * FROM Adverts")
    print(curs.fetchall())

def writeData():
    
if __name__ == "__main__":
    readData()
    #createConnection(db_path)