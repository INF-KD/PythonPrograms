#List of prime number
_upper = input("Enter upper limit :: ")
flag = False
for i in range(2, _upper):
	for j in range(2, i):
		if i % j is 0:
			flag = True
			break
	if flag:
		flag = False
		continue
	else:
		print i