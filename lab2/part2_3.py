from pprint import pprint 
MAXSTUDENTS = 20
MINSTUDENTS = 0
class Student:
    def __init__(self, name, surname, record_book, marks):
        if not isinstance(name, str):
            raise TypeError("Type must be string!")
        self.__name = name
        if not isinstance(surname, str):
            raise TypeError("Type must be string!")
        self.__surname = surname
        self.__record_book = record_book
        if not isinstance(marks, list):
            raise TypeError("Type must be list!")
        self.marks = marks
    
    def __repr__(self):
        return f"{self.name} {self.surname} {self.get_average_mark()}"

    def get_average_mark(self):
    	return sum(self.marks) / len(self.marks)

    def add_marks(self, potential_marks):
        return self.marks.extend(potential_marks)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def record_book(self):
        return self.__record_book

    @staticmethod
    def __str_check(elem):
        if not isinstance(elem, str):
            raise TypeError("Type must be string!")
        elif not elem:
            raise ValueError("No item!")
        else:
            return True

    @name.setter
    def name(self, elem):
        if Client.__str_check(elem):
            self.__name = elem

    @surname.setter
    def surname(self, elem):
        if Client.__str_check(elem):
            self.__surname = elem
        elif not elem:
            raise ValueError("No item!")
        else:
            return True
    @record_book.setter
    def record_book(self, elem):
        if not isinstance(elem, int):
            raise TypeError("Type must be integer!")

            self.__record_book = elem
class Group:
    def __init__(self, group_name, faculty, students):
        self.group_name = group_name
        self.faculty = faculty
        if not isinstance(students, list):
            raise TypeError("Students must be list type!")
        if len(students) <= MAXSTUDENTS and len(students) > MINSTUDENTS:
            self.students = students
        else:
            raise ValueError("Students should be no more than 20 and more than 0!")

    def beststudents(self):
        bests = [item for item in sorted(self.students, reverse=True, key=lambda x: x.get_average_mark())[:5]]
        return bests

    def get_group(self):
        return f"{self.group_name} {self.faculty}"

person1 = Student("Illia", "Vodolieiev", 101, [1, 4, 4, 4, 5])
person2 = Student("Anton", "Dzhulai", 102, [5, 5, 5, 5, 5])
person3 = Student("Dima", "Hohlov", 103, [2, 4, 3, 4, 5])
person4 = Student("Denis", "Zaharia", 104, [5, 5, 4, 2, 5])
person5 = Student("Vladlen", "Haziev", 105, [2, 3, 3, 2, 3])
person6 = Student("Crystyna", "Petrichenko", 106, [5, 4, 3, 3, 4])
person7 = Student("Vlad", "Romanov", 107, [5, 3, 3, 4, 5])
person8 = Student("Ivanna", "Vakuliuk", 108, [2, 3, 2, 1, 5])
person9 = Student("Pavlo", "Nedashkivsky", 109, [4, 2, 4, 4, 5])
person10 = Student("Roman", "Tkachenko", 110, [5, 3, 3, 4, 5])
person11 = Student("Volodimir", "Moroz", 111, [5, 5, 5, 5, 5])
person12 = Student("Vadim", "Loza", 112, [4, 3, 4, 4, 5])
person13 = Student("Serhiy", "Sican", 113, [4, 4, 5, 2, 5])
person14 = Student("Oleksandr", "Rosnov", 114, [4, 5, 3, 4, 5])
person15 = Student("Yarik", "Gruzdov", 115, [4, 4, 5, 4, 5])
person16 = Student("Danil", "Ninadin", 116, [2, 4, 4, 4, 5])
person17 = Student("Liza", "Honchar", 117, [3, 4, 4, 4, 5])
person18 = Student("Dmitro", "Koval", 118, [4, 4, 4, 4, 5])
person19 = Student("Vlad", "Stepoviy", 119, [4, 4, 5, 4, 5])
person20 = Student("Katerina", "Krut", 120, [4, 4, 2, 4, 5])
person2.add_marks([1, 2, 3])
gr = [person1, person2, person3, person4, person5,
        person6, person7, person8, person9, person10, person11,
        person12, person13, person14, person15, person16,
        person17, person18, person19, person20]
group = Group("TI-01", "TEF", gr)
pprint(group.beststudents())

