from Fractal import Fractal

class Julia(Fractal):
	def __init__(self, dictionary, name):
		Fractal.__init__(self, dictionary, name)
		self.complex = complex(float(dictionary["creal"]), float(dictionary["cimag"]))


	def count(self, z):
		for i in range(self.iterations):
			z = z * z + self.complex
			if abs(z) > 2:
				return i 
		return -1
