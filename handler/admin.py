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

print(f"""


           _           _       
          | |         (_)      
  __ _  __| |_ __ ___  _ _ __  
 / _` |/ _` | '_ ` _ \| | '_ \ 
| (_| | (_| | | | | | | | | | |
 \__,_|\__,_|_| |_| |_|_|_| |_|
                               
                               

      """)

#*-------------------------------------------------*#

mydb = functions.connect()

#*-------------------------------------------------*#

#login for admin
name = input("Username: ")
password = input("Password: ")

user = functions.login(mydb, name, password)

if True:
    if mydb is not None:
        help = ("1. list tables + 2. Create table users\n3. get all users + 4. clear database\n5. add admin")
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
            elif choice == "3":
                mycursor = mydb.cursor()
                getAllUsers(mycursor)
                users = mycursor.fetchall()
                print(users)
            elif choice == "4":
                mycursor = mydb.cursor()
                clearDB(mydb)
            elif choice == "5":
                mycursor = mydb.cursor()
                name = input("Name: ")
                addAdmin(mydb, name, "admin")
            elif choice == "clear" or choice == "cls":
                os.system('cls')
                say.say("cleared", "success")
            elif choice == "exit" or choice == "quit":

                break
    else:
        say.say("Connection failed", "error")

else:
    say.say("Login failed", "error")

#*-------------------------------------------------*#       


#*-------------------------------------------------*#