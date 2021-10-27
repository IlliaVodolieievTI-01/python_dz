from math import gcd

class Rational:
	def __init__(self, numerator=1, denominator=1):
		if not isinstance(numerator, int) or not isinstance(denominator, int):
			raise TypeError("Your numbers must be integer!")
		elif not denominator:
			raise ValueError("Denominator cannot be 0!")
		else:
			self.__numerator = numerator
			self.__denominator = denominator
		rdc = gcd(self.__numerator, self.__denominator)
		self.__numerator = self.__numerator // rdc
		self.__denominator = self.__denominator // rdc

	def trade(self):
		return f'{self.__numerator}/{self.__denominator}'

	def calc(self):
		return self.__numerator / self.__denominator


def main():
	firstrational = Rational(9, 12)
	secondrational = Rational(2, 4)
	print(firstrational.trade())
	print(firstrational.calc())
	print(secondrational.trade())
	print(secondrational.calc())


main()




