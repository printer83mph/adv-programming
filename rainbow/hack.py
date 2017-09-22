from termcolor import colored
from random import getrandbits
import sys
from time import sleep

while True:
    if bool(getrandbits(1)):
        if bool(getrandbits(1)):
            sys.stdout.write(colored("0","white"))
        else: sys.stdout.write(colored("1","white"))
    elif bool(getrandbits(1)):
        sys.stdout.write(colored("0","green"))
    else:
        sys.stdout.write(colored("1","green"))
    sleep(0.0005)
