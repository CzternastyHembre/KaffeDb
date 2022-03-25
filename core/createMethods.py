import imp
import sqlite3
from ENV import AllValues, DBname
from ENV import color
from ENV import AllValues


def ppinp(s):
    print(color.GREEN + s + color.END)
    res = input(color.CYAN + "- ")
    print(color.END, end="")
    return res


def pp(l):
    isHeader = True
    m = [max(len(str(l[j][i])) for j in range(len(l)))
         for i in range(len(l[0]))]
    print(color.BOLD, end="")
    for line in l:
        print("| ", end="")
        ls = 1
        for i in range(len(line)):
            el = line[i]
            maxLen = 15
            streng = str(el)

            streng = streng.ljust(
                m[i]) if m[i] < maxLen else streng[0:maxLen].ljust(maxLen)
            ls += len(streng + " | ")
            print(streng, end=" | ")
        if isHeader:

            print("\n" + "-"*ls, end="")
            print(color.END, end="")
            isHeader = False
        print()


def getIdFromList(tableName, header):
    con = sqlite3.connect(DBname)
    c = con.cursor()

    c.execute("SELECT * FROM "+tableName)
    table = c.fetchall()

    con.commit()
    con.close()

    idList = [str(line[0]) for line in table]

    if len(header) > 0:
        tempHeader = ["ID"] + header
        table.insert(0, tempHeader)
    print()
    print(color.YELLOW + color.UNDERLINE + tableName + color.END)
    pp(table)

    res = ppinp("Choose a id for "+tableName+", exit (e)")
    if res.lower() == "e":
        print()
        return False
    if res not in idList:
        print("\nNot a valid ID: try again")
        return getIdFromList(tableName, header)
    return res


def createTable(tableName, setValues, allValues):
    try:
        tableValues = [ppinp(str(value) + ": ")
                       for value in allValues[len(setValues):]]
        for el in tableValues:
            if el.lower() == "e":
                print()
                return
        tableValues = setValues + tableValues

        con = sqlite3.connect(DBname)
        c = con.cursor()

        c.execute("Insert into "+tableName +
                  " ("+str(allValues)[1:-1]+") Values("+str(tableValues)[1:-1]+")")

        con.commit()
        con.close()
        print("\ncreated sucsessfully\n")

    except Exception as e:
        print(e, "try again\n")
        return createTable(tableName, setValues, allValues)


def createUser(user_ID=0):
    createTable("User", [], AllValues["AllUserValues"])


def createBean(user_ID=0):
    createTable("Bean", [], AllValues["AllBeanValues"])


def createFarm(user_ID=0):
    createTable("Farm", [], AllValues["AllFarmValues"])


def createRoastery(user_ID=0):
    createTable("Roastery", [], AllValues["AllRoasteryValues"])


def createProcess(user_ID=0):
    createTable("Process", [], AllValues["AllProcessValues"])


def createBatch(user_ID=0):
    farm_ID = getIdFromList("Farm", AllValues["AllFarmValues"])
    if not farm_ID:
        return
    bean_ID = getIdFromList("Bean", AllValues["AllBeanValues"])
    if not bean_ID:
        return
    process_ID = getIdFromList("Process", AllValues["AllProcessValues"])
    if not process_ID:
        return
    createTable("Batch", [farm_ID, bean_ID, process_ID],
                AllValues["AllBatchValues"])


def createCoffee(user_ID=0):
    batch_ID = getIdFromList("Batch", AllValues["AllBatchValues"])
    if not batch_ID:
        return
    roastery_ID = getIdFromList("Roastery", AllValues["AllRoasteryValues"])
    if not roastery_ID:
        return
    createTable("Coffee", [batch_ID, roastery_ID],
                AllValues["AllCoffeeValues"])


def createContains(user_ID=0):
    bean_ID = getIdFromList("Bean", AllValues["AllBeanValues"])
    if not bean_ID:
        return
    batch_ID = getIdFromList("Batch", AllValues["AllBatchValues"])
    if not batch_ID:
        return
    createTable("Contains", [bean_ID, batch_ID],
                AllValues["AllContainsValues"])


def createProduses_Bean(user_ID=0):
    bean_ID = getIdFromList("Bean", AllValues["AllBeanValues"])
    if not bean_ID:
        return
    farm_ID = getIdFromList("Farm", AllValues["AllFarmValues"])
    if not farm_ID:
        return
    createTable("Produses_Bean", [bean_ID, farm_ID],
                AllValues["AllProduses_BeanValues"])


def createEvaluation(user_ID=0):
    if not user_ID:
        print("You need to log in og create a user to evaluate coffee\n")
        return
    coffee_ID = getIdFromList("Coffee", AllValues["AllCoffeeValues"])
    if not coffee_ID:
        return
    createTable("Evaluation", [coffee_ID, user_ID],
                AllValues["AllEvaluationValues"])
