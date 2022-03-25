import sqlite3
from ENV import DBname


def login():
    user_email = input("Write in user email, exit (e):\n- ")

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
        print("\nNo email "+user_email+": try again\n")
        return login()

    if not passWord(user[0][-1]):
        return login()

    print("Succesfully logged in!\n")
    return user[0][0]


def passWord(pw):
    inp = input("Password exit(e): \n- ")
    if inp.lower() == "e":
        return False
    if inp == pw:
        return True
    print("wrong password, try again: \n")
    return passWord(pw)
