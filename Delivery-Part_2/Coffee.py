import core.createMethods as createMethods
import core.loginMethods as loginMethods
import core.userStories as userStories
import core.fetch as fetch
from ENV import color


def errorp(s):  # Print for errormessage
    print(color.RED + "\n", s, "is not regonized try again:" + color.END)


# Emptyfuntion for the dictionary methods["Fetch"]["All"] so calling it doesn't do anything
def emptyFunc(empptyString):
    pass


methods = {"Create": {  # Dictionary that has functions to run
    "Batch": createMethods.createBatch,
    "Bean": createMethods.createBean,
    "Coffee": createMethods.createCoffee,
    "Contains": createMethods.createContains,
    "Evaluation": createMethods.createEvaluation,
    "Farm": createMethods.createFarm,
    "Process": createMethods.createProcess,
    "Produses_Bean": createMethods.createProduses_Bean,
    "Roastery": createMethods.createRoastery,
    "User": createMethods.createUser,
},
    "Fetch": {
        "All": emptyFunc,
        "Batch": fetch.fetchTable,
        "Bean": fetch.fetchTable,
        "Coffee": fetch.fetchTable,
        "Contains": fetch.fetchTable,
        "Evaluation": fetch.fetchTable,
        "Farm": fetch.fetchTable,
        "Process": fetch.fetchTable,
        "Produses_Bean": fetch.fetchTable,
        "Roastery": fetch.fetchTable,
        "User": fetch.fetchTable,
},
    "Login": loginMethods.login,

    "UserStories": {
        "1": userStories.userStoryOne,
        "2": userStories.userStoryTwo,
        "3": userStories.userStoryTree,
        "4": userStories.userStoryFour,
        "5": userStories.userStoryFive,
}

}
queryString = {
    "Create": "what do you want to create?",
    "Fetch": "what do you want to fetch?",
    "UserStories": "what do userstory do you want?",

}


def ppIntro():  # Pretty print when starting the app
    print("\n" + color.BLUE + color.BOLD +
          "Welcome to the coffee database:" + color.END)
    print(color.GREEN + "I this script you are able to insert insert rows in the different tables")
    print("To view the userstories, simply write :'UserStories'" + color.END)
    print(color.DARKCYAN +
          "Tips: You only need to input the first characters to choose category" + color.END)
    print(color.PURPLE +
          "PS: All the dates is formated 'DD-MM-YYYY', but there is not any validation for that\n" + color.END)


def ppinp(s, l):  # Pritty print for input
    print(color.GREEN + s + color.END)
    print(ppList(l))
    res = input(color.CYAN + "- ")
    print(color.END, end="")
    return res


def ppList(l):  # Pretty print function for the meny choices
    return " |".join([" " + color.BLUE + str(val) + color.END for val in l]) + " "


def completeInput(inp, values):  # Autocomplete for input
    temp = [val for val in values if val[:len(inp)].lower() == inp.lower()]
    if len(temp):
        inp = temp[0]
    return inp


def main():
    user_id = 0
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

        print()

    # Login method
        if inp == "Login":
            user_id = methods[inp]()
            print()
            continue

        inp2 = ""
        while True:
            inp2 = ppinp(queryString[inp],
                         list(methods[inp].keys()) + ["Exit (e)"])
            if inp2.lower() == "e":
                print()
                break

            inp2 = completeInput(inp2, methods[inp].keys())

            if inp2 not in methods[inp]:
                errorp(inp2)
                continue

    # Create methods
            print()
            if inp == "Create":
                print("Creating " + inp2)
                methods[inp][inp2](user_id)  # Den her er sylfrekk da

    # UserStories
            if inp == "UserStories":
                methods[inp][inp2]()

    # Fetch methods
            if inp == "Fetch":
                print("Fetching " + inp2)
                if inp2 == "All":
                    for k, v in methods[inp].items():
                        v(k)
                else:
                    methods[inp][inp2](inp2)


main()
