from random import getrandbits
from termcolor import colored

def printrainbowy(stuff):
    output = ""
    for i in range(len(stuff)):
        if i % 6 == 0:
            output += colored(stuff[i],"red")
        elif (i + 1) % 6 == 0:
            output += colored(stuff[i],"white")
        elif (i + 2) % 6 == 0:
            output += colored(stuff[i],"yellow")
        elif (i + 3) % 6 == 0:
            output += colored(stuff[i],"green")
        elif (i + 4) % 6 == 0:
            output += colored(stuff[i],"blue")
        elif (i + 5) % 6 == 0:
            output += colored(stuff[i],"magenta")
    print output

def printhacker(stuff):
    output = ""
    for i in stuff:
        if bool(getrandbits(1)):
            output += colored(i,"green")
        else:
            output += colored(i,"white")
    print output
