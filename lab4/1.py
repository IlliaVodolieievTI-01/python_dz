from math import gcd

class Rational:
	def __init__(self, numerator=1, denominator=1):
		if not isinstance(numerator, (float, int)) or not isinstance(denominator,(float, int)):
			raise TypeError("Your numbers must be integer!")
		elif not denominator:
			raise ValueError("Denominator cannot be 0!")
		self.__numerator = numerator
		self.__denominator = denominator
		
	def reduce_form(self, num, denum):
		rdc = gcd(num, denum)
		num = num // rdc
		denum = denum // rdc
		return num, denum


	def __str__(self):
		if self.__denominator == 1:
			return f'{self.__numerator}'
		return f'{self.__numerator}/{self.__denominator}'

	def calc(self):
		return self.__numerator / self.__denominator
    
	def getnum(self):
		return self.__numerator

	def getdenum(self):
		return self.__denominator

	def rational_check(self, elem):
		if not isinstance(elem, (Rational, int)):
			raise ArithmeticError("Right operand must be Rational tipe!")
		return None

	def __add__(self, other):
		if not isinstance(other, int):
			self.__numerator, self.__denominator = self.reduce_form(self.__numerator*other.getdenum() + self.__denominator*other.getnum(), self.__denominator*other.getdenum())
			return Rational(self.__numerator, self.__denominator)
		self.__numerator = self.__numerator / self.__denominator + other
		self.__denominator = 1
		return Rational(self.__numerator, self.__denominator)
	
	def __sub__(self, other):
		if not isinstance(other, int):
			self.__numerator, self.__denominator = self.reduce_form(self.__numerator*other.getdenum() - self.__denominator*other.getnum(), self.__denominator*other.getdenum())
			return Rational(self.__numerator, self.__denominator)
		self.__numerator = self.__numerator / self.__denominator + other
		self.__denominator = 1
		return Rational(self.__numerator, self.__denominator)

	def __mul__(self, other):
		if not isinstance(other, int):
			self.__numerator, self.__denominator = self.reduce_form(self.__numerator*other.getnum(), self.__denominator*other.getdenum())
			return Rational(self.__numerator, self.__denominator)
		self.__numerator = self.__numerator / self.__denominator * other
		self.__denominator = 1
		return Rational(self.__numerator, self.__denominator)

	def __truediv__(self, other):
		if not isinstance(other, int):
			self.__numerator, self.__denominator = self.reduce_form(self.__numerator*other.getdenum(), self.__denominator*other.getnum())
			return Rational(self.__numerator, self.__denominator)
		self.__numerator = self.__numerator / self.__denominator / other
		self.__denominator = 1
		return Rational(self.__numerator, self.__denominator)

def main():
	firstrational = Rational(9, 12)
	secondrational = Rational(2, 4)
	firstrational1 = Rational(6, 9)
	secondrational1 = Rational(9, 18)
	firstrational2 = Rational(2, 4)
	secondrational2 = Rational(5, 15)
	firstrational3 = Rational(3, 6)
	secondrational3 = Rational(16, 4)
	rat4 = Rational(12, 6)
	rat5 = Rational(12, 6)
	rat6 = Rational(12, 6)
	rat7 = Rational(12, 6)
	i1, i2 = 3, 4
	thirdrational = firstrational + secondrational
	thirdrational1 = firstrational1 - secondrational1
	thirdrational2 = firstrational2 * secondrational2
	thirdrational3 = firstrational3 / secondrational3
	rat5 = rat5 + i1
	rat4 = thirdrational - i1
	rat6 = rat6 / i1
	rat7 = rat7 * i1
	print(thirdrational)
	print(thirdrational1)
	print(thirdrational2)
	print(thirdrational3)
	print(rat5)
	print(rat4)
	print(rat6)
	print(rat7)



main()