from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter:
	def __init__(self, fractal, gradient):
		self.fractal = fractal
		self.gradient = gradient
		self.min = (fractal.centerx - (fractal.axislength * 0.5), fractal.centery - (fractal.axislength * 0.5))
		self.max = (fractal.centerx + (fractal.axislength / 2.0), fractal.centery + (fractal.axislength / 2.0))



	def display(self):
		window = Tk()
		pixel_size = abs(self.max[0] - self.min[0]) / self.fractal.pixels
		photo = PhotoImage(self.fractal.name, width=self.fractal.pixels, height=self.fractal.pixels)
		canvas = Canvas(window, width=self.fractal.pixels, height=self.fractal.pixels, bg=self.gradient.getColor(0))
		canvas.pack()
		canvas.create_image((self.fractal.pixels / 2, self.fractal.pixels / 2), image=photo, state="normal")
	
		for row in range(self.fractal.pixels, 0, -1):
			for column in range(self.fractal.pixels):
				x = self.min[0] + (column * pixel_size)
				y = self.min[1] + (row * pixel_size)
				color = self.gradient.getColor(self.fractal.count(complex(x,y)))
				photo.put(color, (column, self.fractal.pixels - row))

			window.update()  # display a row of pixels
		photo.write(f"{photo}.png")
		print(f"Wrote image {photo}.png")

		mainloop()


	
