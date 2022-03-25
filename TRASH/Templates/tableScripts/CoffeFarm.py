import sqlite3
from ENV import DBname
tableName = "CoffeeFarm"


def createDB():
    con = sqlite3.connect(DBname)

    c = con.cursor()
    # Create a table
    c.execute("Drop table " + tableName)
    c.execute("CREATE TABLE "+tableName + " (\
              ID TEXT PRIMARY KEY,\
                  name TEXT,\
                      moh INTEGER\
               )")
    con.commit()
    con.close()


def addFarm(id, name, moh):
    con = sqlite3.connect(DBname)
    c = con.cursor()
    c.execute("Insert into "+tableName +
              " Values (?,?,?)", (id, ''+name+'', moh))
    con.commit()
    con.close()


def addFarms():
    farms = [
        [0, "haslum farm", 115],
        [1, "leangen farm", 222]
    ]
    for f in farms:
        addFarm(f[0], f[1], f[2])
