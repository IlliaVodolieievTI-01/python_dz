#	Client         Product
#         \       /
#  		    Order


class Client:
	def __init__(self, name, surname, patronymic, telephone):
		self.name = name
		self.surname = surname
		self.patronymic = patronymic
		self.telephone = telephone

	def clientdata(self):
		return f" Client {self.name} {self.surname} {self.patronymic} {self.telephone}"

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