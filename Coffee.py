import core.createMethods as createMethods
import core.fetchOnPK as fetchOnPK


def pp(s):
    print()
    for line in s:
        for el in line:
            print(el, end=" | ")
        print()
    print()


methods = {"create": {"User": createMethods.createUser,
                      "Bean": createMethods.createBean,
                      "Farm": createMethods.createFarm,
                      "Roastery": createMethods.createRoastery,
                      "Process": createMethods.createProcess,

                      },
           "fetch": {"user": fetchOnPK.fetchUserOnPK,
                     "bean": fetchOnPK.fetchBeanOnPK}
           }

while True:
    inp = input("what do you want to do?: " +
                str(list(methods.keys()))[1:-1]+", exit (e)\n- ")
    if inp.lower() == "e":
        break

    if inp not in methods:
        print(inp, "is not regonized try againt:\n")
        continue

    inp2 = ""
    while inp2 != "e":
        inp2 = input("\nwhat do you want to "+inp+"? : " +
                     str(list(methods[inp].keys()))[1:-1]+", exit (e)\n- ")
        if inp2.lower() == "e":
            break
        if inp2 not in methods[inp]:
            print(inp, "is not regonized try againt:\n")
            continue
        pp(methods[inp][inp2]())  # Den her er sylfrekk da
        break
