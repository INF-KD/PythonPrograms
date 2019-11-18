def factorial(num):
	fact = 1
	while num is not 0:
		fact = fact * num
		num = num - 1
	return fact
def recFactorial(num):
	if num is 1:
		return 1
	else:
		return num*recFactorial(num-1)
print factorial(input("Enter number for factorial :: "))
print "Recursion factorial method ::", recFactorial(5)