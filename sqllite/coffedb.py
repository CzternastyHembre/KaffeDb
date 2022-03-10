import sqlite3
con = sqlite3.connect("test.db")
cursor = con.cursor()
l = [
"INSERT INTO Person VALUES (1, 'Ola');",
"INSERT INTO Person VALUES (2, 'Kari');",
"INSERT INTO Person VALUES (3, 'Per');",
"INSERT INTO Person VALUES (4, 'Liv');",
"INSERT INTO Person VALUES (5, 'Nora');",
"INSERT INTO Person VALUES (6, 'Lukas');",
]
for e in l:   
    cursor.execute(e)
    con.commit()


cursor.execute("""
select * from Person where "Pnr" > 4
"""
)
print(cursor.fetchall())
con.close()