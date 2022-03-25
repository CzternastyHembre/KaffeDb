import sqlite3
from ENV import DBname
from core.createMethods import ppinp
from ENV import color


def login():
    user_email = ppinp("Write in user email, exit (e)")

    if user_email.lower() == "e":
        return

    con = sqlite3.connect(DBname)
    c = con.cursor()

    c.execute("SELECT user_ID, user_email, password FROM User")
    users = c.fetchall()

    con.commit()
    con.close()

    user = [val for val in users if val[1] == user_email]
    if not user:
        print(color.RED + "\nNo email "+user_email+": try again\n" + color.END)
        return login()

    if not passWord(user[0][-1]):
        return login()

    print("Succesfully logged in!\n")
    return user[0][0]


def passWord(pw):
    inp = ppinp("Password exit(e):")
    if inp.lower() == "e":
        return False
    if inp == pw:
        return True
    print(color.RED + "wrong password, try again: \n" + color.END)
    return passWord(pw)
