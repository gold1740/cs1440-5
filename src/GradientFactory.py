from BlackWhite import BlackWhite
from DefaultGradient import DefaultGradient 

def makeGradient(iterations, gtype):	
	if iterations <= 0:
		print("iteration count must be greater than 0")
		exit(-1)
	if gtype == None:
		return DefaultGradient(iterations)
	elif gtype.lower() == "blackwhite":
		return BlackWhite(iterations)

	elif gtype.lower() == "defaultgradient":
		return DefaultGradient(iterations)

	else:
		print("invalid gradient name")
		exit(-1)
