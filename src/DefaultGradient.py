from Gradient import Gradient
from colour import Color

class DefaultGradient(Gradient):
	def __init__(self, steps):
		self.gradient = list(Color("#ffe4b5").range_to("#002277", steps))

	def getColor(self, n):
		return self.gradient[n]





