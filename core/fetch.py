import sqlite3
from ENV import DBname

from core.createMethods import pp

from core.userStories import fetchAllFromQuery
from ENV import AllValues
from ENV import color


def fetchTable(tableName):
    table = fetchAllFromQuery("SELECT * FROM " + tableName, [])
    if not tableName == "Contains":
        table.insert(0, ["ID"] + AllValues[tableName])
    else:
        table.insert(0, AllValues[tableName])

    print(color.YELLOW + color.UNDERLINE + tableName + color.END)
    pp(table)
    print()
    return
