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

def nfib(a):
	num1, num2 = 0,1
	for i in range(a):
		num2,num1 = num1+num2,num2
	return num1
