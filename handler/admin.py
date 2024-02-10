# custom imports
import say
import colors
import functions

from say import *
from colors import *
from functions import *

mydb = functions.connect()

if mydb is not None:
    print("1. list tables\n2. Create table users")
    while True:
        choice = input(f"{yellow}[{lightblack}{name}@{ip}{yellow}]{white} > ")

        if choice == "1":
            mycursor = mydb.cursor()

            mycursor.execute("SHOW TABLES")

            for x in mycursor:
                print(x)
        elif choice == "2":
            mycursor = mydb.cursor()
            TableIfNone(mycursor)

else:
    say.say("Connection failed", "error")