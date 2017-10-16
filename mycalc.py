
import sys
from random import randint

def add(a,b):
	return a + b
def sub(a,b):
	return a - b
def mul(a,b):
	return a * b
def div(a,b):
	return a / b

def fib(a):
	if a == 0: return 0
	if a == 1: return 1
	return(fib(a-1)+fib(a-2))

def ffib(a):
	num1, num2 = 0,1
	oldfinal = 1
	final = 1
	for i in range(a):
		final,num1,num2 = num2+final,num2,oldfinal
		oldfinal = final
	return num1

def nfib(a,index=True):
	num1, num2 = 0,1
	if index:
		for i in range(a):
			num2,num1 = num1+num2,num2
	else:
		while num2<a:
			num2,num1 = num1+num2,num2
	return num1

def montyhall(trials):
	swwins = 0
	stwins = 0
	for i in range(trials):
		goat = randint(0,2)
		choice = randint(0,2)
		if choice == goat:
			swwins += 1
		else:
			if randint(0,1):
				swwins += 1
	for i in range(trials):
		goat = randint(0,2)
		choice = randint(0,2)
		if choice == goat:
			stwins += 1
	print(swwins,"wins when switching",trials-swwins,"losses")
	print(stwins,"wins when staying,",trials-stwins,"losses")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		print nfib(int(sys.argv[1]))