#*-------------------------------------------------*#

import colorama
import socket

from colorama import Fore

#*-------------------------------------------------*#

# Set name 
name = (socket.gethostname())
# set ip 
ip = (socket.gethostbyname(name))
# set all colors that we use
red = "\033[1;31m"
yellow = "\033[1;33m"
purple = "\033[1;35m"
white = "\033[1;37m"
blue = Fore.BLUE
lightblack = Fore.LIGHTBLACK_EX

#*-------------------------------------------------*#