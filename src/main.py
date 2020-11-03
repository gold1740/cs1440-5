import sys

from FractalFactory import makeFractal
from GradientFactory import makeGradient
from ImagePainter import ImagePainter

configFileName = None
if len(sys.argv) > 1:
    configFileName = sys.argv[1]

gradientName = None
if len(sys.argv) > 2:
    gradientName = sys.argv[2]

# When the FractalFactory's argument is None it returns the default fractal
fractal = makeFractal(configFileName)

# When the GradientFactory's gtype argument is None it returns the default gradient
gradient = makeGradient(fractal.iterations, gtype=gradientName)

image = ImagePainter(fractal, gradient)
image.display()
