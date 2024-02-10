import socket

from colors import *

def say(message, type):
    if type == "success":
        print(f"{purple}[{lightblack}{name}@{ip}{purple}]{white} {message}")
    elif type == "error":
        print(f"{red}[{lightblack}{name}@{ip}{red}]{white} {message}")
    elif type == "warning":
        print(f"{yellow}[{lightblack}{name}@{ip}{yellow}]{white} {message}")


# ------------------------------
#
# example:
# say("hello", "success")
#
# ------------------------------

# ------------------------------
#
# todo:
# better formatting
#
# ------------------------------