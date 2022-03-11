"""
Datatypes in sqlite3:
    NULL
    INTEGER - INT
    REAL - DECIMAL
    TEXT - STRING
    BLOB - MP3, MP4...
"""

import tableScripts.coffeeDBBeans as CBeans
import tableScripts.coffeeDBUser as CUser
import tableScripts.CoffeFarm as CFarm
from ENV import DBname

CUser.createDB()
CUser.addUsers()

CBeans.createDB()
CBeans.addBeans()

CFarm.createDB()
CFarm.addFarms()
