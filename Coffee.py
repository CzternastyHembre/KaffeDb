import core.createMethods as createMethods
import core.fetchOnPK as fetchOnPK
import core.loginMethods as loginMethods


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

}


def main():
    user = 1
    while True:
        inp = input("what do you want to do?: " +
                    str(list(methods.keys()))[1:-1]+", exit (e)\n- ")
        if inp.lower() == "e":
            break

        if inp not in methods:
            errorp(inp)
            continue
    # Login method
        if inp == "Login":
            user = methods[inp]()
            continue

        inp2 = ""
        while True:
            inp2 = input("\nwhat do you want to "+inp+"? :\n" +
                         str(list(methods[inp].keys()))[1:-1]+", exit (e)\n- ")
            if inp2.lower() == "e":
                print()
                break

            if inp2 not in methods[inp]:
                errorp(inp2)
                continue

    # Create methods
            if inp == "Create":
                methods[inp][inp2](user)  # Den her er sylfrekk da

    # Fetch methods


main()
