class Rectangle:
	def __init__(self, firstside, secondside):
		self.firstside = firstside
		self.secondside = secondside

	def perimeter(self):
		if self.firstside>0 and self.secondside<20:
			return 2*self.firstside+2*self.secondside
		else:
			return False


	def area(self):
		if self.firstside>0 and self.secondside<20:
			return self.firstside*self.secondside
		else:
			return False

def main():
	firstrectangle = Rectangle(0, 3)
	secondrectangle = Rectangle(4, 5)
	print("Your perimetr: %d" %firstrectangle.perimeter())
	print("Your area: %d" %firstrectangle.area())
	print("Your perimetr: %d" %secondrectangle.perimeter())
	print("Your area: %d" %secondrectangle.area())

main()