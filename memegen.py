
from random import choice

def main():
    with open("words.txt", "r") as wordfile:
        words = wordfile.read().split("\n");
        for i in range(1000):
            print(memeify("When the " + choice(words) + " is really " + choice(words) + " but you " + choice(words) + " and then " + choice(words) + " haha " + choice(words)))

def memeify(word):
    output = word
    for i in range(len(output)):
        if output[i] not in ("a","e","i","o","u"," "):
            output = output[:i] + "b" + output[i+1:]
    return output

main()
