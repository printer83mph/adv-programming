from math import floor

def deepen(low,high,guesses):
    if low + 1 == high: return high
    inp = input("My guess is " + str(floor((high+low)/2)) + "! ")
    if inp == "h":
        return deepen(floor((high+low)/2),high,guesses+1)
    elif inp == "l":
        return deepen(low,floor((high+low)/2),guesses+1)
    elif inp == "y":
        return floor((high+low)/2),guesses

print("Pick a number from 1 to 10000!")
ans = deepen(0,10000,1)
print("Your number is " + str(ans[0]) + ", I got it in " + str(ans[1]) + " trie(s)!")
