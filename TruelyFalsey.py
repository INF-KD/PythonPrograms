#Datatype		TrulyValue		FalseyValue
#int				0			any other int eg, -13, 500
#float				0.0			any other float eg, 2.2, -5.5
#string				""			"Any thing without blank string"

#Used when you want to know variable is blank or not

stringV, integerV, floatV = "", 5, 0

if stringV:
	print "Variable have value", stringV
else:
	print "Variable is blank"

if integerV:
	print "Variable is not blank"
else:
	print "Variable is null or zero"

if not floatV:
	print "Variable is blank"