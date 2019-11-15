# Check prime or not
val = input("Enter any integer :: ")
flag = False
if type(val) is int:
	for i in range(2, val):
		if val % i is 0:
			flag = True
			break #For fast execution
	if flag:
		print "Not prime"
	else:
		print val, "is prime number"
else:
	print "Not look like integer"