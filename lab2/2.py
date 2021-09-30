class Rational:
	__numerator = 1
	__denominator = 2
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def calc(self):
		if self.denominator != 0:
			return self.numerator/self.denominator
		else:
			return False

def main():
	firstrational = Rational(3, 4)
	secondrational = Rational(2, 0)
	print("%f" %firstrational.calc())
	print("%f" %secondrational.calc())

main()



