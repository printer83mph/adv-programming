
import sys

def checkPalindrome(n, index=0):
    return True if index > len(str(n))/2 else False if n[index] != n[-index-1] else checkPalindrome(n,index+1)

print checkPalindrome(sys.argv[1])
