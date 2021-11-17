import json
day_now = 4
min_day = 0
max_day = 8

with open('pizza.json') as f1:
	pizza = json.load(f1)

with open('price.json') as f2:
	price = json.load(f2)

class Pizza:
	def __init__(self, day):
		self.day = day
		self.total_price = 0
		self.name_of_pizza = ""

	def add_products(self, potential_products):
		return self.products.extend(potential_products)

	def order_pizza(self, potential_products):
		if self.name_of_pizza not in price:
			raise ValueError("We don't make it pizza!")
		self.total_price += price[self.name_of_pizza]
		total_products = str(potential_products)
		return f'-------\n{self.name_of_pizza} added to order!\nAdded products:{total_products}\nPrice:{price[self.name_of_pizza]}\nTotal price:{self.total_price}\n-------'

	def order_other_pizza(self, pizza_name, potential_products):
		if pizza_name not in price:
			raise ValueError("We don't make it pizza!")
		self.total_price += price[pizza_name]
		total_products = str(potential_products)
		return f'-------\n{pizza_name} added to order!\nAdded products:{total_products}\nPrice:{price[self.name_of_pizza]}\nTotal price:{self.total_price}\n-------'

	def pizza_of_day(self):
		if self.day < min_day and self.day > max_day:
			raise ValueError("Unreal day!")
		return pizza[self.day]

	def orderprice(self):
		return self.total_price

class Margherita(Pizza):
	def __init__(self):
		super().__init__(day_now)
		self.name_of_pizza = "Margherita"

class Peperoni(Pizza):
	def __init__(self):
		super().__init__(day_now)
		self.name_of_pizza = "Peperoni"

class Chesees(Pizza):
	def __init__(self):
		super().__init__(day_now)
		self.name_of_pizza = "4 Chesees"

class Crudo(Pizza):
	def __init__(self):
		super().__init__(day_now)
		self.name_of_pizza = "Crudo"

class Americana(Pizza):
	def __init__(self):
		super().__init__(day_now)
		self.name_of_pizza = "Americana"

class Marinara(Pizza):
	def __init__(self):
		super().__init__(day_now)
		self.name_of_pizza = "Marinara"

class Prosciutto(Pizza):
	def __init__(self):
		super().__init__(day_now)
		self.name_of_pizza = "Prosciutto"


firstorder = Margherita()
print(firstorder.order_pizza(['Chesee', 'Meet']))
print(firstorder.order_other_pizza('Peperoni', ['Chesee']))
print("Prepare to payment: %.2f$" %firstorder.orderprice())