from Fractal import Fractal

class Mandelfour(Fractal):
	def __init__(self, dictionary, name):
 		Fractal.__init__(self, dictionary, name)



	def count(self, z):
		self.complex = complex(0, 0)
		for i in range(self.iterations):
			self.complex = self.complex ** 4 + z
			
			if abs(self.complex) > 2:
				return i
		return -1
