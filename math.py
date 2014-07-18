import math

def printLog(x):
	if x < 0:
		print "Enter positive number please."
		return
	result = math.log(x)
	print "The log of x is ",result

printLog(2)
