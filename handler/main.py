#*-------------------------------------------------*#

import say
import colors
import functions

from say import *
from colors import *
from functions import *

#*-------------------------------------------------*#

try:
    functions.connect()
except:
    say.say("Connection failed", "error")

#*-------------------------------------------------*#
    
print("1. register user        2. login")
    
choice = input(f"{yellow}[{lightblack}{name}@{ip}{yellow}]{white} > ")



#*-------------------------------------------------*#
    
if choice == "1":
    # example of registering a user
    connection = functions.connect()

    name = input("Username: ")
    password = input("Password: ")
    hassPass = hash(password)

    functions.addUser(connection, name, hassPass)

if choice == "2":
    connection = functions.connect()

    name = input("Username: ")
    password = input("Password: ")

    user = functions.login(connection, name, password)

    if True:
        say.say("Logged in", "success")
        say.say("Welcome, " + name, "success")
    else:
        say.say("Login failed", "error")
else:
    say.say("Invalid choice", "error")


#*-------------------------------------------------*#