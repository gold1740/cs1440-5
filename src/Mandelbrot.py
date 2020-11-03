from Fractal import Fractal

class Mandelbrot(Fractal):
	def __init__(self, dictionary, name): 
		Fractal.__init__(self, dictionary, name)


	def count(self, c):
		self.complex = complex(0, 0)
		for i in range(self.iterations):
			self.complex = self.complex * self.complex + c

			if abs(self.complex) > 2:
				return i
		return -1
