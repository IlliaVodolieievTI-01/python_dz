#	Client         Product
#         \       /
#  		    Order


class Client:
    def __init__(self, name, surname, patronymic, telephone):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.telephone = telephone

    def clientdata(self):
        return f" Client {self.__name} {self.__surname} {self.__patronymic} {self.telephone}"

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def patronymic(self):
        return self.__patronymic

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

    @patronymic.setter
    def patronymic(self, elem):
        if Client.__str_check(elem):
            self.__patronymic = elem

class Product:
    def __init__(self, productname, price, weight, tax):
        self.productname = productname
        self.price = price
        self.weight = weight
        self.tax = tax

    def  productdata(self):
        return f" Product {self.productname} {self.price} {self.weight} {self.tax}"

class Order(Client, Product):
    def __init__(self, name, surname, patronymic, telephone, productname, price, weight, tax):
        Client.__init__(self, name, surname, patronymic, telephone)
        Product.__init__(self, productname, price, weight, tax)

    def fullprice(self):
        return self.price * self.tax

firstorder = Order('Ivan', 'Pervashin', 'Olecsiyovich', 38097456283, 'water', 300, 30, 2)
print(firstorder.clientdata())
print(firstorder.productdata())
print("Total price: ")
print(firstorder.fullprice())
