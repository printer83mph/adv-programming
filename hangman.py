from random import choice

def play(wordlist,tries):
    word = choice(wordlist)
    triesleft = tries
    guessedletters = ""
    gamefinished = False
    while gamefinished == False:
        letterguess = raw_input("What letter? ")[0].lower()
        guessedletters += letterguess
        if letterguess not in word:
            triesleft -= 1
            print "Nope"
        else: print "Yup!"
        output = word
        for i in output:
            if i not in guessedletters: i = "_"
        print output
        print triesleft, " tries left."
        if triesleft == 0:
            print "Game over!"
            gamefinished = True
        elif set(word).issubset(set(guessedletters)):
            print "You win!"
            gamefinished = True

if __name__ == "__main__":
    play(["wassup","pasta"],10)
