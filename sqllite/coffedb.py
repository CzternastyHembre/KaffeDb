import sqlite3

con = sqlite3.connect("coffe.db")
cursor = con.cursor()
l = [
"INSERT INTO Person VALUES (1, 'Ola');",
"INSERT INTO Person VALUES (2, 'Kari');",
"INSERT INTO Person VALUES (3, 'Per');",
"INSERT INTO Person VALUES (4, 'Liv');",
"INSERT INTO Person VALUES (5, 'Nora');",
"INSERT INTO Person VALUES (6, 'Lukas');",
]
