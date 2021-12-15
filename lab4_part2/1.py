from abc import ABC, abstractmethod

class ICourseFactory(ABC):
	@abstractmethod
	def setSpecialization(self):
		pass

class ICourse(ICourseFactory):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def setTeacher(self):
		pass

	@abstractmethod
	def setPlan(self):
		pass

class ITeacher(ICourseFactory):
	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def setName(self):
		pass

	@abstractmethod
	def setSurname(self):
		pass

	@abstractmethod
	def setPatronymic(self):
		pass

	@abstractmethod
	def setExperience(self):
		pass

class ILocalCourse(ICourse):
	@abstractmethod
	def setAudithory(self):
		pass

class IOffsiteCourse(ICourse):
	@abstractmethod
	def setPlace(self):
		pass

class Course(ICourseFactory):
	def __init__(self, specialization, teacher, plan):
		if not isinstance(specialization, str):
			raise TypeError("Wrong type!")
		self.specialization = specialization
		if not isinstance(teacher, Teacher):
			raise TypeError("Wrong type!")
		self.teacher = teacher
		if not isinstance(plan, list):
			raise TypeError("Wrong type!")
		self.plan = plan

	def setSpecialization(self, specialization):
		self.specialization = specialization

	def setTeacher(self, teacher):
		self.teacher = teacher

	def setPlan(self, plan):
		self.plan = plan

	def getCourse(self):
		return f'Specialization: {self.specialization}\nPlan: {self.plan}'
	
class LocalCourse(Course):
	def __init__(self, specialization, teacher, plan, audithory):
		super().__init__(specialization, teacher, plan)
		if not isinstance(audithory, int):
			raise TypeError("Wrong type!")
		self.audithory = audithory

	def setAudithory(self, audithory):
		self.audithory = audithory

	def getLocal(self):
		return self.getCourse() + f'\nAudithory: {self.audithory}'

class OffsiteCourse(Course):
	def __init__(self, specialization, teacher, plan, place):
		super().__init__(specialization, teacher, plan)
		if not isinstance(place, str):
			raise TypeError("Wrong type!")
		self.place = place

	def setPlace(self, place):
		self.place = place

	def getLocal(self):
		return self.getCourse() + f'\nPlace: {self.place}'

class Teacher(ITeacher):
	def __init__(self, specialization, name, surname, patronymic, experience):
		if not isinstance(specialization, str):
			raise TypeError("Wrong type!")
		self.specialization = specialization
		if not isinstance(name, str):
			raise TypeError("Wrong type!")
		self.name = name
		if not isinstance(surname, str):
			raise TypeError("Wrong type!")
		self.surname = surname
		if not isinstance(patronymic, str):
			raise TypeError("Wrong type!")
		self.patronymic = patronymic
		if not isinstance(experience, int):
			raise TypeError("Wrong type!")
		self.experience = experience

	def setSpecialization(self, specialization):
		self.specialization = specialization

	def setName(self, name):
		self.name = name

	def setSurname(self, surname):
		self.surname = surname

	def setPatronymic(self, patronymic):
		self.patronymic = patronymic

	def setExperience(self, experience):
		self.experience = experience

	def getTeacher(self):
		return f'Name: {self.name}\nSurname: {self.surname}\nPatronymic: {self.patronymic}\nExperience: {self.experience}'


t1 = Teacher("Illia", "Vodolieiv", "Oleck" , "IT", 12) 

c1 = LocalCourse("IT", t1, ['math', 'language'], 142)
print(c1.getLocal())
print(t1.getTeacher())