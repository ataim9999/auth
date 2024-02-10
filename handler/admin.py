#*-------------------------------------------------*#
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
    help = ("1. list tables + 2. Create table users")
    while True:
        choice = input(f"{yellow}[{lightblack}{name}@{ip}{yellow}]{white} > ")
        if choice == "help":
            say.say((help), "warning")
        elif choice == "1":
            mycursor = mydb.cursor()
            mycursor.execute("SHOW TABLES")
            for x in mycursor:
                print(x)
        elif choice == "2":
            mycursor = mydb.cursor()
            TableIfNone(mycursor)

        elif choice == "3":
            mycursor = mydb.cursor()
            getAllUsers(mycursor)
            users = mycursor.fetchall()
            print(users)
        elif choice == "clear" or choice == "cls":
            os.system('cls')
            say.say("cleared", "success")
        elif choice == "exit" or choice == "quit":

            break


else:
    say.say("Connection failed", "error")

#*-------------------------------------------------*#