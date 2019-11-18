def printName(fnm, lnm, orderReverse=False):
	if not orderReverse:
		print fnm, lnm
	else:
		print lnm, fnm
printName("Karmdip", "Devmurari")
printName("John", "Doe", True)