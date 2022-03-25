import core.createMethods as createMethods
import core.fetchOnPK as fetchOnPK
import core.loginMethods as loginMethods
from ENV import color


def pp(s):
    print()
    for line in s:
        for el in line:
            print(el, end=" | ")
        print()
    print()


def errorp(s):
    print("\n", s, "is not regonized try againt:")


methods = {"Create": {
    "Batch": createMethods.createBatch,
    "Bean": createMethods.createBean,
    "Coffee": createMethods.createCoffee,
    "Evaluation": createMethods.createEvaluation,
    "Farm": createMethods.createFarm,
    "Process": createMethods.createProcess,
    "Produses_Bean": createMethods.createProduses_Bean,
    "Roastery": createMethods.createRoastery,
    "User": createMethods.createUser,
},
    "Fetch": {
        "user": fetchOnPK.fetchUserOnPK,
        "bean": fetchOnPK.fetchBeanOnPK
},
    "Login": loginMethods.login,

    "UserStories": {
        "1": "TISS",
        "2": "TISS",
        "3": "TISS",
        "4": "TISS",
        "5": "TISS",
}

}


def ppIntro():
    print("\n" + color.BLUE + color.BOLD +
          "Welcome to the coffee database:" + color.END)
    print(color.GREEN + "I this script you are able to insert insert rows in the different tables")
    print("To view the userstories, simply write :'UserStories'" + color.END)
    print(color.DARKCYAN +
          "Tips: You only need to input the first characters to choose category\n" + color.END)


def ppinp(s, l):
    print(color.GREEN + s + color.END)
    print(ppList(l))
    res = input(color.CYAN + "- ")
    print(color.END, end="")
    return res


def ppList(l):
    return " |".join([" " + color.BLUE + str(val) + color.END for val in l]) + " "


def completeInput(inp, values):
    temp = [val for val in values if val[:len(inp)].lower() == inp.lower()]
    if len(temp):
        inp = temp[0]
    return inp


def main():
    user = 1
    ppIntro()
    while True:
        inp = ppinp("what do you want to do?:",
                    list(methods.keys()) + ["Exit (e)"]
                    )
        if inp.lower() == "e":
            break

        inp = completeInput(inp, methods.keys())
        if inp not in methods:
            errorp(inp)
            continue
    # Login method
        if inp == "Login":
            user = methods[inp]()
            continue

        inp2 = ""
        while True:
            inp2 = ppinp("what do you want to "+inp+"?",
                         list(methods[inp].keys()) + ["Exit (e)"])
            if inp2.lower() == "e":
                print()
                break

            inp2 = completeInput(inp2, methods[inp].keys())

            if inp2 not in methods[inp]:
                errorp(inp2)
                continue

    # Create methods
            if inp == "Create":

                methods[inp][inp2](user)  # Den her er sylfrekk da

    # Fetch methods


main()
