# custom imports
import say
import functions

try:
    functions.connect()
except:
    say.say("Connection failed", "error")