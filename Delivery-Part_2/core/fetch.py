import sqlite3
from ENV import DBname

from core.createMethods import pp

from core.userStories import fetchAllFromQuery
from ENV import AllValues
from ENV import color


def fetchTable(tableName):  # Function that prints the table based on the tablename
    table = fetchAllFromQuery("SELECT * FROM " + tableName, [])
    if tableName == "Contains" or tableName == "Produses_Bean":
        table.insert(0, AllValues[tableName])
    else:
        table.insert(0, ["ID"] + AllValues[tableName])

    print(color.YELLOW + color.UNDERLINE + tableName + color.END)
    pp(table)
    print()
    return
