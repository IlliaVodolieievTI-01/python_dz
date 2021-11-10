import json

with open('pizza.json') as f1:
	pizza = json.load(f1)

with open('price.json') as f2:
	price = json.load(f2)

class Pizza:
	def __init__(self, day):
		self.day = day
		self.total_price = 0

	def add_products(self, potential_products):
		return self.products.extend(potential_products)

	def order_pizza(self, name_of_pizza, potential_products):
		if name_of_pizza not in price:
			raise ValueError("We don't make it pizza!")
		self.total_price += price[name_of_pizza]
		total_products = str(potential_products)
		return f'-------\n{name_of_pizza} added to order!\nAdded products:{total_products}\nPrice:{price[name_of_pizza]}\nTotal price:{self.total_price}\n-------'

	def pizza_of_day(self):
		if self.day < 0 and self.day > 8:
			raise ValueError("Unreal day!")
		return pizza[self.day]

	def orderprice(self):
		return self.total_price


firstorder = Pizza(4)
print(firstorder.order_pizza('Margherita', ['Chesee', 'Meet']))
print(firstorder.order_pizza('Peperoni', ['Chesee']))
print("Prepare to payment: %.2f$" %firstorder.orderprice())



