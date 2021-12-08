import math

"""Constants and Dictionaries"""
MAXMOUNTH = 12
MINMOUNTH = 0
MAXDAY = 31
MINDAY = 0
ITER = 1

yr = {
	1 : 31,
	2 : 28,
	3 : 31,
	4 : 30,
	5 : 31,
	6 : 30,
	7 : 31,
	8 : 31,
	9 : 30,
	10 : 31,
	11 : 30,
	12 : 31
}

"""Main class"""
class Calendar:
	def __init__(self, d, m, y):
		if not MINDAY < d <= MAXDAY:
			ValueError("Wrong value!")
		self.day = d
		if not MINMOUNTH < m <= MAXMOUNTH:
			ValueError("Wrong value!")
		self.mounth = m
		self.year = y
	
	"""String output"""
	def __str__(self):
		return f'{self.day}.{self.mounth}.{self.year}'
	
	"""Day output"""
	@property
	def day(self):
		return self.__day

	"""Mounth output"""
	@property
	def mounth(self):
		return self.__mounth
	
	"""Year output"""
	@property
	def year(self):
		return self.__year

	@day.setter
	def day(self, value):
		if not isinstance(value, int):
			raise TypeError("Wrong type!")
		elif not MINDAY < value <= MAXDAY:
			raise ValueError("Wrong value!")
		self.__day = value

	@mounth.setter
	def mounth(self, value):
		if not isinstance(value, int):
			raise TypeError("Wrong type!")
		elif not MINMOUNTH < value <= MAXMOUNTH:
			raise ValueError("Wrong value!")
		self.__mounth = value
	
	@year.setter
	def year(self, value):
		if not isinstance(value, int):
			raise TypeError("Wrong type!")
		self.__year = value

	"""Operator overloads +=, -=, >, <, >=, <="""
	def __iadd__(self, other):
		if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
			yr["2"] += 1
			if self.mounth + other.mounth > MAXMOUNTH:
				self.mounth += other.mounth - MAXMOUNTH
				self.year += ITER
			else:
				self.mounth += other.mounth
			if self.day + other.day > yr1[self.mounth]:
				self.day = self.day + other.day - yr1[self.mounth]
				self.mounth += ITER
			else:
				self.day += other.day
			self.year += other.year
			yr["2"] -= 1
		else:
			if self.mounth + other.mounth > MAXMOUNTH:
				self.mounth += other.mounth - MAXMOUNTH
				self.year += ITER
			else:
				self.mounth += other.mounth
			if self.day + other.day > yr[self.mounth]:
				self.day = self.day + other.day - yr[self.mounth]
				self.mounth += ITER
			else:
				self.day += other.day
			self.year += other.year
			return Calendar(self.day, self.mounth, self.year)

	def __isub__(self, other):
		if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
			yr["2"] += 1
			if self.day - other.day < yr1[self.mounth - other.mounth]:
				self.day = self.day - other.day + yr1[self.mounth - other.mounth]
				self.mounth -= ITER
			else:
				self.day -= other.day
			if self.mounth - other.mounth <= MINMOUNTH:
				self.mounth =self.mounth - other.mounth + MAXMOUNTH
				self.year -= ITER
			else:
				self.mounth -= other.mounth
			self.year -= other.year
			yr["2"] -= 1
		else:
			if self.day - other.day < yr[self.mounth - other.mounth]:
				self.day = self.day - other.day + yr[self.mounth - other.mounth]
				self.mounth -= ITER
			else:
				self.day -= other.day
			if self.mounth - other.mounth <= MINMOUNTH:
				self.mounth =self.mounth - other.mounth + MAXMOUNTH
				self.year -= ITER
			else:
				self.mounth -= other.mounth
			self.year -= other.year
		return Calendar(self.day, self.mounth, self.year)

	def __eq__(self, other):
		if self.year != other.year and self.mounth != other.day and self.year != other.day:
			return False
		return True

	def __ne__(self, other):
		if self.year != other.year and self.mounth != other.day and self.year != other.day:
			return True
		return False

	def __lt__(self, other):
		if self.year < other.year:
			return True
		elif self.year > other.year:
			return False
		else:
			if self.mounth < other.mounth:
				return True
			elif self.mounth > other.mounth:
				return False
			else:
				if self.day < other.day:
					return True
				elif self.day > other.day:
					return False
				return False

	def __gt__(self, other):
		if self.year > other.year:
			return True
		elif self.year < other.year:
			return False
		else:
			if self.mounth > other.mounth:
				return True
			elif self.mounth < other.mounth:
				return False
			else:
				if self.day > other.day:
					return True
				elif self.day < other.day:
					return False
				return False

	def __le__(self, other):
		if self < other or self == other:
			return True
		return False
	
	def __ge__(self, other):
		if self > other or self == other:
			return True
		return False


def main():
	c1 = Calendar(12, 2, 2010)
	c2 = Calendar(30, 4, 5)
	c3 = Calendar(11, 2, 2010)
	c4 = Calendar(12, 1, 7)
	c5 = Calendar(12, 1, 7)
	c1 += c2
	c3 -= c4
	print(c1)
	print(c3)
	print(c2<c4)
	print(c4>c2)
	print(c1<=c2)
	print(c4>=c5)

main()