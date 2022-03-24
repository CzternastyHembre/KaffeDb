import sqlite3
from core.ENV import DBname
tableName = "CoffeeBeans"


def createDB():
    con = sqlite3.connect(DBname)
    c = con.cursor()
    # Create a table
    c.execute("Drop table " + tableName)
    c.execute("CREATE TABLE "+tableName+" (\
              species TEXT PRIMARY KEY\
              )")
    con.commit()
    con.close()


def addBean(specie):
    con = sqlite3.connect(DBname)
    c = con.cursor()
    c.execute("Insert into "+tableName+" Values ('"+specie+"')")
    con.commit()
    con.close()


def addBeans():
    species = ["coffea arabica", "coffea robusta", "coffea liberica"]
    for s in species:
        addBean(s)
