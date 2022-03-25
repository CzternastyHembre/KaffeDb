import sqlite3
from ENV import DBname

AllBeanValues = ["bean_name", "species"]
AllFarmValues = ["farm_name", "country", "region", "height"]
AllRoasteryValues = ["roastery_name", "region", "country"]
AllProcessValues = ["process_name", "description"]
AllUserValues = ["user_email", "first_name", "last_name", "password"]

AllBatchValues = ["farm_ID", "bean_ID",
                  "process_ID", "harvestYear", "kg_price_usd"]
AllCoffeeValues = ["batch_ID", "roastery_ID", "coffee_name",
                   "roast_degree", "kg_price_kr", "coffee_description", "roast_date"]
AllContainsValues = ["bean_ID", "batch_ID"]
AllProduses_BeanValues = ["bean_ID", "farm_ID"]
AllEvaluationValues = ["coffee_ID", "user_ID",
                       "points", "evalutation_date", "user_notes"]


def pp(l):
    isHeader = True
    m = [max(len(str(l[j][i])) for j in range(len(l)))
         for i in range(len(l[0]))]
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
    print(tableName)
    pp(table)

    res = input("\nChoose a id for "+tableName+", exit(e):\n- ")
    if res.lower() == "e":
        return False
    if res not in idList:
        print("\nNot a valid ID: try again")
        return getIdFromList(tableName, header)
    return res


def createTable(tableName, setValues, allValues):
    try:
        tableValues = [input(str(value) + ": ")
                       for value in allValues[len(setValues):]]
        for el in tableValues:
            if el.lower() == "e":
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
    createTable("User", [], AllUserValues)


def createBean(user_ID=0):
    createTable("Bean", [], AllBeanValues)


def createFarm(user_ID=0):
    createTable("Farm", [], AllFarmValues)


def createRoastery(user_ID=0):
    createTable("Roastery", [], AllRoasteryValues)


def createProcess(user_ID=0):
    createTable("Process", [], AllProcessValues)


def createBatch(user_ID=0):
    farm_ID = getIdFromList("Farm", AllFarmValues)
    if not farm_ID:
        return
    bean_ID = getIdFromList("Bean", AllBeanValues)
    if not bean_ID:
        return
    process_ID = getIdFromList("Process", AllProcessValues)
    if not process_ID:
        return
    createTable("Batch", [farm_ID, bean_ID, process_ID], AllBatchValues)


def createCoffee(user_ID=0):
    batch_ID = getIdFromList("Batch", AllBatchValues)
    if not batch_ID:
        return
    roastery_ID = getIdFromList("Roastery", AllRoasteryValues)
    if not roastery_ID:
        return
    createTable("Coffee", [batch_ID, roastery_ID], AllCoffeeValues)


def createContains(user_ID=0):
    bean_ID = getIdFromList("Bean", AllBeanValues)
    if not bean_ID:
        return
    batch_ID = getIdFromList("Batch", AllBatchValues)
    if not batch_ID:
        return
    createTable("Contains", [bean_ID, batch_ID], AllContainsValues)


def createProduses_Bean(user_ID=0):
    bean_ID = getIdFromList("Bean", AllBeanValues)
    if not bean_ID:
        return
    farm_ID = getIdFromList("Farm", AllFarmValues)
    if not farm_ID:
        return
    createTable("Produses_Bean", [bean_ID, farm_ID], AllProduses_BeanValues)


def createEvaluation(user_ID=0):
    if not user_ID:
        print("You need to log in og create a user to evaluate coffee\n")
        return
    coffee_ID = getIdFromList("Coffee", AllCoffeeValues)
    if not coffee_ID:
        return
    createTable("Evaluation", [user_ID, coffee_ID], AllEvaluationValues)
