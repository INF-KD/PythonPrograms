def result(*subs):
	tot = 0
	ind = 1
	failed = ()
	for i in subs:
		tot = tot + i
		if i < 40:
			failed = failed + (ind,)
		ind = ind + 1
	print "Failed in subjects...", failed
	return "Total is ", tot
print result(50, 60, 30, 40, 80)