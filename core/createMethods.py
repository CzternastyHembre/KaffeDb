import sqlite3
from ENV import DBname


def createUser():
    try:
        user_email = input("unique email (e): ")
        firstName = input("firstName (e): ")
        lastName = input("lastName (e): ")
        password = input("password (e): ")
        if user_email.lower() == "e" or firstName.lower() == "e" or lastName.lower() == "e" or password.lower() == "e":
            return
        con = sqlite3.connect(DBname)
        c = con.cursor()

        c.execute("Insert into User Values (?,?,?,?)",
                  (user_email, firstName, lastName, password))
        con.commit()
        con.close()
        print("created sucsessfully")
#        print(c.fetchone("Select * from Bean where beanID == "+bean))

    except Exception as e:
        print(e, "Try again")
        createUser()


def createBean():
    try:
        bean_ID = int(input("bean_ID: "))
        bean_name = input("bean_name (e): ")
        species = input("species (e): ")
        if bean_name.lower() == "e" or species.lower() == "e":
            return
        con = sqlite3.connect(DBname)
        c = con.cursor()

        c.execute("Insert into Bean Values (?,?,?)",
                  (bean_ID, bean_name, species))
        print("created sucsessfully")
        c.execute("Select * from Bean where Bean.bean_ID == " +
                  str(bean_ID))  # OBS er dette dårlig
        print(c.fetchone())
        con.commit()
        con.close()

    except Exception as e:
        print(e, "Try again")
        createBean()
