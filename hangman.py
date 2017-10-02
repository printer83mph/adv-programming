from random import choice
'''
def play(wordlist,tries):
    word = choice(wordlist)
    triesleft = tries
    guessedletters = ""
    gamefinished = False
    while gamefinished == False:
        output = word
        for i in range(len(output)):
            if output[i] not in guessedletters:
                output = "%s%s%s"%(output[:i],"_",(output[i+1:]))
        print output
        print triesleft, " tries left."
        letterguess = raw_input("What letter? ")[0].lower()
        if letterguess not in word:
            if letterguess in guessedletters:
                print "Already used!"
            else:
                print "Nope"
                triesleft -= 1
        else: print "Yup!"
        guessedletters += letterguess
        if triesleft == 0:
            print "Game over! The word was ", word
            gamefinished = True
        elif set(word).issubset(set(guessedletters)):
            print "You win! the word was ", word
            gamefinished = True

if __name__ == "__main__":
    wl = open("words.txt","r")
    words = wl.read().split("\n")
    play(words,6)

'''
def play(wordlist,tries):
    word,triesleft,guessedletters,gamefinished = choice(wordlist),tries,"",False
    while gamefinished == False:
        output = word
        for i in range(len(output)):
            if output[i] not in guessedletters: output = "%s%s%s"%(output[:i],"_",(output[i+1:]))
        print output,"\n",triesleft, " tries left."
        letterguess = raw_input("What letter? ")[0].lower()
        if letterguess not in word: 
            if letterguess in guessedletters: print "Already used!"
            else: print "Nope"; triesleft -= 1
        else: print "Yup!"
        guessedletters += letterguess
        if triesleft == 0: print "Game over! The word was ", word; gamefinished = True
        elif set(word).issubset(set(guessedletters)): print "You win! the word was ", word; gamefinished = True

if __name__ == "__main__":
    wl = open("words.txt","r")
    words = wl.read().split("\n")
    play(words,6)
