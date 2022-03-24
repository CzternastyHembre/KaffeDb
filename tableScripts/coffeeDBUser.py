import sqlite3
from core.ENV import DBname

# con = sqlite3.connect(':memory:') lagres kun i minne


def createDB():
    con = sqlite3.connect(DBname)

    # Create cursos

    c = con.cursor()
    # Create a table

    c.execute("Drop table users")
    c.execute("""CREATE TABLE Users (
    email TEXT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    password TEXT
    )
    """)
    con.commit()
    con.close()


def addUser(email, fname, lname, p):
    con = sqlite3.connect(DBname)
    c = con.cursor()
    c.execute("Insert into Users Values (?,?,?,?)", (email, fname, lname, p))
    con.commit()
    con.close()


def addUsers():
    firstnames = ["Mattis", "Casper", "Karan", "Sofus"]
    lastnames = ["Hembre", "Amtrup", "Singhn", "Buskover"]
    passwords = ["1234567", "Password", "Mom123", "Icecream"]
    for fname in firstnames:
        for lname in lastnames:
            email = (fname + "." + lname).lower() + "@gmail.com"
            addUser(email, fname, lname, passwords[firstnames.index(fname)])
