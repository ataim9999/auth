# custom imports
import say
import colors
import functions

from say import *
from colors import *
from functions import *

#*-------------------------------------------------*#

import os

os.system('cls && title admin.py')

#*-------------------------------------------------*#

mydb = functions.connect()

if mydb is not None:
    help = ("1. list tables + 2. Create table users\n 3. ... + 4. ...")
    while True:
        choice = input(f"{yellow}[{lightblack}{name}@{ip}{yellow}]{white} > ")

        if choice == "help":
            print(help)
        elif choice == "1":
            mycursor = mydb.cursor()

            mycursor.execute("SHOW TABLES")

            for x in mycursor:
                print(x)
        elif choice == "2":
            mycursor = mydb.cursor()
            TableIfNone(mycursor)

        elif choice == "exit":
            break

else:
    say.say("Connection failed", "error")

#*-------------------------------------------------*#