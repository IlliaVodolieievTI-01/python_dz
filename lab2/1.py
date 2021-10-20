class Rectangle:
	def __init__(self, firstside, secondside):
		if not isinstance(firstside, int) and  not isinstance(firstside, float) or not isinstance(secondside, int) and not isinstance(secondside, float):
			raise TypeError("Sides must be integer or float!")
		elif firstside<=0 or firstside>20 or secondside<=0 or secondside>20:
			raise ValueError("Bad value...")
		else:
			self.firstside = firstside
			self.secondside = secondside

	def perimeter(self):
		return 2*self.firstside+2*self.secondside


	def area(self):
		return self.firstside*self.secondside

def main():
	firstrectangle = Rectangle(1, 3)
	secondrectangle = Rectangle(4, 5)
	print("Your perimetr: %d" %firstrectangle.perimeter())
	print("Your area: %d" %firstrectangle.area())
	print("Your perimetr: %d" %secondrectangle.perimeter())
	print("Your area: %d" %secondrectangle.area())

main()