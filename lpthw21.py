def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(20, 5)
height = subtract(76, 4)
weight = multiply (85, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d." % (age, height, weight, iq)

#a puzzle for extra credit
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes,", what, "\nCan you do it by hand?"