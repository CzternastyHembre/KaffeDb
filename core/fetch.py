import sqlite3
from ENV import DBname

from core.createMethods import pp

from core.userStories import fetchAllFromQuery


def fetchTable(tableName):
    table = fetchAllFromQuery("SELECLT * FROM " + tableName)
    pass


def fetchUserOnPK():
    try:
        user_id = input("user ID (e): ")
        if user_id == "e":
            return

        con = sqlite3.connect(DBname)
        c = con.cursor()

        c.execute("Select * from User where User.user_ID == " +
                  user_id)  # OBS er dette dårlig tror ikke det går
        res = c.fetchone()
        con.commit()
        con.close()
        return [res]
    except Exception as e:
        print(e, " try again: \n")
        fetchUserOnPK()


def fetchBeanOnPK():
    try:
        beanID = input("bean ID (e): ")
        if beanID == "e":
            return

        con = sqlite3.connect(DBname)
        c = con.cursor()

        c.execute("Select * from Bean where Bean.bean_ID == " +
                  beanID)  # OBS er dette dårlig
        res = c.fetchone()
        con.commit()
        con.close()
        return [res]
    except Exception as e:
        print(e, " try again: \n")
        fetchBeanOnPK()
