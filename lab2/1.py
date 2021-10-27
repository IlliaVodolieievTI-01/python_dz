MAXLEN = 20
MINLEN = 0
class Rectangle:
	def __init__(self, firstside, secondside):
		self.__firstside = firstside
		self.__secondside = secondside

	def get_firstside(self):
		return self.__firstside

	def get_secondside(self):
		return self.__secondside

	def set_firstside(self):
		if not isinstance(firstside, int) and  not isinstance(firstside, float):
			raise TypeError("Sides must be integer or float!")
		elif firstside<=MINLEN or firstside>MAXLEN:
			raise ValueError("Bad value...")
		else:
			self.__firstside = firstside


	def set_secondside(self):
		if not isinstance(secondside, int) and  not isinstance(secondside, float):
			raise TypeError("Sides must be integer or float!")
		elif secondside<=MINLEN or secondside>MAXLEN:
			raise ValueError("Bad value...")
		else:
			self.__secondside = secondside

	def perimeter(self):
		return 2*self.__firstside+2*self.__secondside


	def area(self):
		return self.__firstside*self.__secondside

def main():
	firstrectangle = Rectangle(1, 3)
	secondrectangle = Rectangle(4, 5)
	print("Your perimetr: %d" %firstrectangle.perimeter())
	print("Your area: %d" %firstrectangle.area())
	print("Your perimetr: %d" %secondrectangle.perimeter())
	print("Your area: %d" %secondrectangle.area())

main()