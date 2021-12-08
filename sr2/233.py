class Human:
	def __init__(self, surname, name, patronymic, date_of_birthday, sex):
		if not isinstance(surname, str):
			raise TypeError("Wrong type!")
		self.surname = surname
		if not isinstance(name, str):
			raise TypeError("Wrong type!")
		self.name = name
		if not isinstance(patronymic, str):
			raise TypeError("Wrong type!")
		self.patronymic = patronymic
		if not isinstance(date_of_birthday, str):
			raise TypeError("Wrong type!")
		self.date_of_birthday = date_of_birthday
		if not isinstance(sex, str):
			raise TypeError("Wrong type!")
		self.sex = sex

	@property
	def surname(self):
		return self.surname

	@property
	def name(self):
		return self.name

	@property
	def patronymic(self):
		return self.patronymic

	@property
	def date_of_birthday(self):
		return self.date_of_birthday

	@property
	def sex(self):
		return self.sex
	
	@staticmethod
	def __str_check(elem):
		if not isinstance(elem, str):
 			raise TypeError("Type must be string!")
		elif not elem:
			raise ValueError("No item!")
		else:
			return True

	@surname.setter
	def surname(self, elem):
 		if Human.__str_check(elem):
			 self.surname = elem

	@name.setter
	def name(self, elem):
 		if Human.__str_check(elem):
			 self.name = elem

	@patronymic.setter
	def patronymic(self, elem):
 		if Human.__str_check(elem):
			 self.patronimic = elem

	@date_of_birthday.setter
	def date_of_birthday(self, elem):
 		if Human.__str_check(elem):
			 self.date_of_birthday = elem

	@sex.setter
	def sex(self, elem):
 		if Human.__str_check(elem):
			 self.sex = elem


class Employee(Human):
	def __init__(self, surname, name, patronymic, date_of_birthday, sex, organization, specialization, position, salary, experience):
		super().__init__(surname, name, patronymic, date_of_birthday, sex)
		if Human.__str_check(organization):
			self.organization = organization
		if Human.__str_check(specialization):
			self.specialization = specialization
		if Human.__str_check(position):
			self.position = position
		if not isinstance(salary, int):
			raise TypeError("Wrong type!")
		self.salary = salary
		if not isinstance(experience, int):
			raise TypeError("Wrong type!")
		self.experience = experience

	@property
	def organization(self):
		return self.organization

	@property
	def specialization(self):
		return self.specialization
	
	@property
	def position(self):
		return self.position
	
	@property
	def salary(self):
		return self.salary
	
	@property
	def experience(self):
		return self.experience

	@organization.setter
	def organization(self, elem):
 		if Human.__str_check(elem):
			 self.organization = elem
			 
	@specialization.setter
	def specialization(self, elem):
 		if Human.__str_check(elem):
			 self.specialization = elem

	@position.setter
	def position(self, elem):
 		if Human.__str_check(elem):
			 self.position = elem

	@salary.setter
	def salary(self, elem):
		if not isinstance(elem, int):
			 raise TypeError("Wrong type!")
		self.salary = elem

	@experience.setter
	def experience(self, elem):
		if not isinstance(elem, int):
			 raise TypeError("Wrong type!")
		self.experience = elem

class Organization:
	def __init__(self, employees):
		if not isinstance(employees, list):
			raise TypeError("Wrong type!")
		itr = SimpleIterator(len(employees))
		for i in employees:
			if not isinstance(i, Employee):
				raise TypeError("Wrong type!")
		self.employees = employees
		self.sorted_list = []

	def exp(self, value):
		for i in self.employees:
			if i.experience > value:
				self.sorted_list.append(i)
		return self.sorted_list

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

em1 = Employee("Vodolieiev", "Illia", "Oleksiyovich", "31/12/2000", "M", "Viva", "IT", "junior", 300, 1)
em2 = Employee("Haziev", "Illia", "Oleksiyovich", "31/12/1999", "M", "Viva", "IT", "junior", 500, 2)
em3 = Employee("Koliev", "Illia", "Oleksiyovich", "31/12/1992", "M", "Viva", "IT", "Middle", 1000, 5)
em4 = Employee("Rediev", "Illia", "Oleksiyovich", "31/10/1999", "M", "Viva", "IT", "junior", 400, 3)
org1 = Organization(em1, em2, em3, em4)
print(org1.exp(2))