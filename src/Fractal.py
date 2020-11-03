class Fractal:
	def __init__(self, dictionary, name):
		self.iterations = dictionary["iterations"]
		self.pixels = dictionary["pixels"]
		self.centerx = dictionary["centerx"]
		self.centery = dictionary["centery"]
		self.axislength = dictionary["axislength"]
		self.name = name.split('/')[-1]
		
		
	def count(self, z):
		raise NotImplementedError
