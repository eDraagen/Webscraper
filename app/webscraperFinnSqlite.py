import sqlite3
from sqlite3 import Error

#//TODO: Need to look up on CSV and import it into sqliteDb, Import the webscraper script and that creates a cvs file and sends it to this script, and import it into the database.

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

def readData():
    curs.execute("SELECT * FROM Adverts")
    print(curs.fetchall())



if __name__ == "__main__":
    createConnection(db_path)
    readData()