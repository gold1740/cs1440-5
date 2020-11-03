from Julia import Julia
from Mandelbrot import Mandelbrot
from Mandelfour import Mandelfour


def makeFractal(cfgfile=None):
	if cfgfile == None:
		return Mandelbrot({"pixels": 640, "centerx": 0.0, "centery": 0.0,"axislength": 4.0,"iterations": 100})
		
	dictionary = {}
	lines = open(cfgfile).readlines()
	
	for i in lines:
		if i.startswith('#') or i.startswith('\n'):
			continue
		line = i.split(":")
		dictionary[line[0].strip()] = line[1].strip()


	try:
		dictionary["type"]
		dictionary["pixels"]
		dictionary["centerx"]
		dictionary["centery"]
		dictionary["axislength"]
		dictionary["iterations"]
	except KeyError:
		print("Config file is missing a data field or something is misspelled")
		exit(-1)

	else:
		choice = dictionary["type"]
		
		if (choice == "mandelbrot"):
			toConstruct = Mandelbrot
		elif (choice == "julia"):
			toConstruct = Julia
		elif (choice == "mandelbrot4"):
			toConstruct = Mandelfour
		else:
			print("Fractal type invalid")
			exit(-1)

	dictionary["pixels"] = int(dictionary["pixels"])
	dictionary["centerx"] = float(dictionary["centerx"])
	dictionary["centery"] = float(dictionary["centery"])
	dictionary["axislength"] = float(dictionary["axislength"])
	dictionary["iterations"] = int(dictionary["iterations"]) 

	return toConstruct(dictionary, cfgfile[:-5])
