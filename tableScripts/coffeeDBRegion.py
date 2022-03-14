import sqlite3
from ENV import DBname
tableName = "Region"


def createDB():
    con = sqlite3.connect(DBname)

    c = con.cursor()
    # Create a table
    #c.execute("Drop table " + tableName)
    c.execute("CREATE TABLE "+tableName + " (\
        Name TEXT PRIMARY KEY\
        CountryName TEXT\
        FOREIGN KEY(CountryName) REFERENCES Country(name)\
        )")
    con.commit()
    con.close()


def addRegion(name):
    con = sqlite3.connect(DBname)
    c = con.cursor()
    c.execute("Insert into " + tableName + " Values (?)", ([name]))
    con.commit()
    con.close()


def addRegions():
    countries = [
        ["Stavanger", "Norway"],
        ["Botogá", "Colombia"],
        ["Stockholm", "Sweeden"]
    ]
    for c in countries:
        addRegions(c)
