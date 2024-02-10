# custom imports
import say
import colors
import functions

from colors import *

mydb = functions.connect()

if mydb is not None:
    choice = input(f"{yellow}[{lightblack}{name}@{ip}{yellow}]{white} > ")

    if choice == "1":
        mycursor = mydb.cursor()

        mycursor.execute("SHOW TABLES")

        for x in mycursor:
            print(x)
else:
    say.say("Connection failed", "error")