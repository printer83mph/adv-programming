
from random import choice

def main():
    with open("words.txt", "r") as wordfile:
        outputfile = open("output","w")
        wordlists = []
        for list in wordfile.read().split(":"):
            wordlists.append(list.split("\n"))
        for i in range(100):
            outputfile.write(("When the " + choice(wordlists[0]) + " is " + choice(wordlists[1]) + " and you " + choice(wordlists[2]) + " but then " + choice(wordlists[3])) + "\n")

def memeify(word):
    output = word
    for i in range(len(output)):
        if output[i] not in ("a","e","i","o","u"," "):
            output = output[:i] + "b" + output[i+1:]
    return output

main()
