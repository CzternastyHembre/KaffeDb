import sqlite3
from ENV import DBname


def fetchUserOnPK():
    user_email = input("unique email (e): ")
    if user_email == "e":
        return

    con = sqlite3.connect(DBname)
    c = con.cursor()

    c.execute("Select * from User where User.user_email == " +
              user_email)  # OBS er dette dårlig tror ikke det går
    print(c.fetchone())
    con.commit()
    con.close()


"""
    try:
    except Exception as e:
        print(e)
"""


def fetchBeanOnPK():
    try:
        beanID = input("bean ID (e): ")
        if beanID == "e":
            return

        con = sqlite3.connect(DBname)
        c = con.cursor()

        c.execute("Select * from Bean where Bean.bean_ID == " +
                  beanID)  # OBS er dette dårlig
        print("\nBean \n", c.fetchone(), "\n")
        con.commit()
        con.close()
    except Exception as e:
        print(e)
