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

yr1 = {
	1 : 31,
	2 : 29,
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
		if(d > MAXDAY and d < MINDAY):
			ValueError("Wrong value!")
		self.day = d
		if(m > MAXMOUNTH and m < MINMOUNTH):
			ValueError("Wrong value!")
		self.mounth = m
		self.year = y
	
	"""String output"""
	def __str__(self):
		return f'{self.day}.{self.mounth}.{self.year}'
	
	"""Day output"""
	def get_day(self):
		return self.day

	"""Mounth output"""
	def get_mounth(self):
		return self.mounth
	
	"""Year output"""
	def get_year(self):
		return self.year

	"""Operator overloads +=, -=, >, <, >=, <="""
	def __iadd__(self, other):
		if self.year % 4 == 0:
			if self.mounth + other.get_mounth() > MAXMOUNTH:
				self.mounth += other.get_mounth() - MAXMOUNTH
				self.year += ITER
			else:
				self.mounth += other.get_mounth()
			if self.day + other.get_day() > yr1[self.mounth]:
				self.day = self.day + other.get_day() - yr1[self.mounth]
				self.mounth += ITER
			else:
				self.day += other.get_day()
			self.year += other.get_year()
		else:
			if self.mounth + other.get_mounth() > MAXMOUNTH:
				self.mounth += other.get_mounth() - MAXMOUNTH
				self.year += ITER
			else:
				self.mounth += other.get_mounth()
			if self.day + other.get_day() > yr[self.mounth]:
				self.day = self.day + other.get_day() - yr[self.mounth]
				self.mounth += ITER
			else:
				self.day += other.get_day()
			self.year += other.get_year()
			return Calendar(self.day, self.mounth, self.year)

	def __isub__(self, other):
		if self.year % 4 == 0:
			if self.day - other.get_day() < yr1[self.mounth - other.get_mounth()]:
				self.day = self.day - other.get_day() + yr1[self.mounth - other.get_mounth()]
				self.mounth -= ITER
			else:
				self.day -= other.get_day()
			if self.mounth - other.get_mounth() <= MINMOUNTH:
				self.mounth =self.mounth - other.get_mounth() + MAXMOUNTH
				self.year -= ITER
			else:
				self.mounth -= other.get_mounth()
			self.year -= other.get_year()
		else:
			if self.day - other.get_day() < yr[self.mounth - other.get_mounth()]:
				self.day = self.day - other.get_day() + yr[self.mounth - other.get_mounth()]
				self.mounth -= ITER
			else:
				self.day -= other.get_day()
			if self.mounth - other.get_mounth() <= MINMOUNTH:
				self.mounth =self.mounth - other.get_mounth() + MAXMOUNTH
				self.year -= ITER
			else:
				self.mounth -= other.get_mounth()
			self.year -= other.get_year()
		return Calendar(self.day, self.mounth, self.year)

	def __eq__(self, other):
		if self.year != other.get_year() and self.mounth != other.get_day() and self.year != other.get_day():
			return False
		return True

	def __ne__(self, other):
		if self.year != other.get_year() and self.mounth != other.get_day() and self.year != other.get_day():
			return True
		return False

	def __lt__(self, other):
		if self.year < other.get_year():
			return True
		elif self.year > other.get_year():
			return False
		else:
			if self.mounth < other.get_mounth():
				return True
			elif self.mounth > other.get_mounth():
				return False
			else:
				if self.day < other.get_day():
					return True
				elif self.day > other.get_day():
					return False
				return False

	def __gt__(self, other):
		if self.year > other.get_year():
			return True
		elif self.year < other.get_year():
			return False
		else:
			if self.mounth > other.get_mounth():
				return True
			elif self.mounth < other.get_mounth():
				return False
			else:
				if self.day > other.get_day():
					return True
				elif self.day < other.get_day():
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