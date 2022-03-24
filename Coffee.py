from ENV import DBname
import core.createMethods as createMethods
import core.fetchOnPK as fetchOnPK

methods = {"create": {"user": createMethods.createUser,
                      "bean": createMethods.createBean},
           "fetch": {"user": fetchOnPK.fetchUserOnPK,
                     "bean": fetchOnPK.fetchBeanOnPK}
           }

inp = ""
while inp.lower() != "e":
    inp = input("what do you want to do?" +
                str(methods.keys())+" exit: (e)\n- ")

    if inp not in methods:
        print(inp, "is not regonized try againt:\n")
        continue

    inp2 = ""
    while inp2 != "e":
        inp2 = input("\nwhat do you want to "+inp+" :" +
                     str(methods[inp].keys())+"\n- ")
        if inp2 not in methods[inp]:
            print(inp, "is not regonized try againt:\n")
            continue
        methods[inp][inp2]()  # Den her er sylfrekk da
        break
