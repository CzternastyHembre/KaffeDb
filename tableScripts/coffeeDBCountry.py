import sqlite3
from core.ENV import DBname
tableName = "Country"


def createDB():
    con = sqlite3.connect(DBname)

    c = con.cursor()
    # Create a table
    c.execute("Drop table " + tableName)
    c.execute("CREATE TABLE "+tableName + " (\
        name TEXT PRIMARY KEY\
        CONSTRAINT Country_PK PRIMARY KEY (Pnr)); \
            );")
    con.commit()
    con.close()


def addCountry(name):
    con = sqlite3.connect(DBname)
    c = con.cursor()
    c.execute("Insert into " + tableName + " Values (?)", ([name]))
    con.commit()
    con.close()


def addCountries():
    countries = [
        "Norway",
        "Colombia",
        "Sweeden"
    ]
    for c in countries:
        addCountry(c)
