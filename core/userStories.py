import os
import sqlite3
from ENV import DBname
from ENV import color
from core.createMethods import pp
import datetime


def fetchAllFromQuery(query, vars):
    con = sqlite3.connect(DBname)
    c = con.cursor()

    c.execute(query, vars)
    table = c.fetchall()

    con.commit()
    con.close()
    return table


def userStoryOne():
    print("Simply to the following steps:")
    print("- 1 First use the fetch command in the terminal to see if the exisiting rows exist")
    print("- 2 Then create the rows that are needed")
    print("- 3 Then create a Evaluation with the parameters")
    print()


def userStoryTwo():
    current_year = datetime.datetime.now().year
    yearformat = "%" + str(current_year)

    table = fetchAllFromQuery("""SELECT first_name, last_name, COUNT(DISTINCT coffee_ID) AS types
    FROM User
    NATURAL JOIN Evaluation
        WHERE evalutation_date LIKE ?
    GROUP BY user_ID
    ORDER BY types DESC""", [yearformat])

    table = [(val[2], val[0] + " " + val[1]) for val in table]
    table.insert(0, ["Taste types", "Full name"])
    print(color.YELLOW + color.UNDERLINE + "Userstory 2" + color.END)
    pp(table)
    print()


def userStoryTree():
    table = fetchAllFromQuery("""
    """)
