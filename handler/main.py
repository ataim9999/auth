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
    
# example of registering a user
connection = functions.connect()

name = input("Username: ")
password = input("Password: ")

functions.addUser(connection, name, password)

#*-------------------------------------------------*#