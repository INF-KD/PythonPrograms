def isPrime(num):
	flag = True
	for i in range(2, num):
		if num % i is 0:
			flag = False
			break
	return flag
print isPrime(9)
if isPrime(13):
	print "Entered number is prime"
else:
	print "Not prime"