import colorama
import socket

from colorama import Fore

name = (socket.gethostname())
ip = (socket.gethostbyname(name))
red = "\033[1;31m"
yellow = "\033[1;33m"
purple = "\033[1;35m"
white = "\033[1;37m"
lightblack = Fore.LIGHTBLACK_EX