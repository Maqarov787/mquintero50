#Marco Quintero
#Ghidorah
#skeleton/stub :: SQLITE3 BASICS
#10-18-24

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
def dbCommands():
    fin = ""
    for row in reader:
        fin += f"(row['code'], row['mark'], row['id'])\n"
    print(fin)
    return fin

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
dbCommands()
command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
