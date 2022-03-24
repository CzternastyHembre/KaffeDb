import sqlite3

from numpy import vsplit
from core.ENV import DBname


def createTable(tableName, idName, values):
    try:
        tableValues = []
        for value in values:
            tableValues.append(input(str(value) + ": "))
        for el in tableValues:
            if el.lower() == "e":
                return

        con = sqlite3.connect(DBname)
        c = con.cursor()

        valueString = "(" + "?," * len(tableValues)
        valueString = valueString[:-1] + ")"
        print(valueString)

        c.execute("Insert into "+tableName+" Values "+valueString, tableValues)
        c.execute("Select * from "+tableName+" where "+tableName + "." + idName+" == " +
                  tableValues[0])  # OBS er dette dårlig
        res = c.fetchone()
        con.commit()
        con.close()

        print(res)
        print("created sucsessfully")
        return [res]
    except Exception as e:
        print(e, "try again\n")
        createTable(tableName, idName, values)


def createUser():
    createTable("User", "user_id", ["user_id", "user_email",
                "firstName", "lastName", "password"])


def createBean():
    createTable("Bean", "bean_id", ["bean_ID", "bean_name", "species"])


def createFarm():
    createTable("Farm", "farm_ID",
                ["farm_id", "farm_name", "country", "region", "height"])


def createRoastery():
    createTable("Roastery", "roastery_ID",
                ["Roastery_id", "Roastery_name", "region", "country"])


def createProcess():
    createTable("Process", "process_ID",
                ["Process_id", "Process_name", "description"])
