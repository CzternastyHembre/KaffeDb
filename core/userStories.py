import os
import sqlite3
from ENV import AllValues, DBname
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
    print("- 1 Log in or create a user")
    print("- 2 First use the fetch command in the terminal to see if the exisiting rows exist")
    print("- 3 Then create the rows that are needed")
    print("- 4 Then create a Evaluation with the parameters")
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
    table = fetchAllFromQuery("""SELECT avg(points) as avg_points,kg_price_kr, coffee_name, roastery_name
FROM Evaluation
    NATURAL JOIN Coffee
    NATURAL JOIN Roastery
GROUP BY Coffee.coffee_ID
ORDER BY avg_points / kg_price_kr DESC;""", [])
    table.insert(0, ["avg points", "kg price", "coffee name", "roastery name"])
    pp(table)
    print()


def userStoryFour():
    anyFloral = "%floral%"
    table = fetchAllFromQuery("""SELECT coffee_name, roastery_name
FROM Coffee
    NATURAL JOIN Roastery
    NATURAL JOIN Evaluation
WHERE (Evaluation.user_notes LIKE ? OR Coffee.coffee_description LIKE ?)
""", [anyFloral] * 2)
    table.insert(0, ["Coffee name", "Roastery name"])
    pp(table)
    print()


def userStoryFive():
    countryOne = "Rwanda"
    countryTwo = "Colombia"
    descType = "%washed%"
    table = fetchAllFromQuery("""SELECT coffee_name, roastery_name
FROM Coffee
    NATURAL JOIN Batch
    NATURAL JOIN Roastery
    INNER JOIN Farm on Farm.farm_ID == Batch.farm_ID
    NATURAL JOIN Process
    NATURAL JOIN Contains
WHERE (Roastery.country=? OR Roastery.country=? OR Farm.country=? OR Farm.country=?) AND NOT ((description== ?) OR (process_name == ?) OR (coffee_description == ?))
""", [countryOne, countryTwo]*2 + [descType] * 3)
    table.insert(0, ["Coffee name", "Roastery name"])
    pp(table)
    print()
