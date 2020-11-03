from Gradient import Gradient
from colour import Color

class BlackWhite(Gradient):
	def __init__(self, steps):
		self.gradient = list(Color("#000000").range_to("#ffffff", steps))



	def getColor(self, n):
		return self.gradient[n]
