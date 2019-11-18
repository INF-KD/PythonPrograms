def monthDays(month):
	_31 = ("jan", "march", "may", "july", "aug", "oct", "dec", "january", "august", "octomber", "december")
	_30 = ("april", "june", "sept", "nov", "september", "november")
	if type(month) is str:		
		m = month.lower()
		if m in _31:
			return 31
		elif m in ("feb", "february"):
			return 28
		elif m in _30:
			return 30
		else:
			return "Not valid month"
	else:
		if month in (1, 3, 5, 7, 8, 10, 12):
			return 31
		elif month is 2:
			return 28
		elif month > 12:
			return "Not valid month"
		else:
			return 30
print monthDays(10)