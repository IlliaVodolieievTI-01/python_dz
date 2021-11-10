import uuid
import json

with open('base_data.json') as f:
	data = json.load(f)
default_price = data['default_price']
days_before = data['days_before']

class Ticket:
	def __init__(self, price, days):
		self.id = uuid.uuid4()
		if not isinstance(price, (int, float)):
			raise TypeError("Price must be integer or float!")
		self.price = price
		if not isinstance(days, int):
			raise TypeError("Days must be integer!")
		self.days = days
		self.type_of_ticket = ""
		self.data_id = {}

	def create_ticket(self, id):
		if not len(str(id)) == 36:
			raise TypeError("Id must be have 36 symbols!")
		self.id = id
		self.data_id[self.id] = [str(self.type_of_ticket)]
		self.data_id[self.id].append(str(self.days))
		self.data_id[self.id].append(str(self.price))
		with open('data.json', 'w') as f1:
			json.dump(self.data_id, f1)

	def get_info(self, value_id):
		with open('data.json') as f2:
			data_id = json.load(f2)
		if value_id not in data_id:
			raise ValueError("Not found this id!")
		for id in data_id.keys():
			if value_id == id:
				return f"{value_id} --- {str(data_id[value_id])}"

	def get_price(self):
		return self.price

	def __str__(self):
		return f"-------\n{self.type_of_ticket}ticket\nId: {self.id}\nPrice: {self.price}\n-------"

class Defaultticket(Ticket):
	def __init__(self):
		super().__init__(default_price, days_before)
		self.price = default_price
		self.type_of_ticket = "Default"
		self.id = uuid.uuid4()

class Earlyticket(Ticket):
	def __init__(self):
		super().__init__(default_price, days_before)
		if days_before < 60:
			raise ValueError("Unreal create Earlyticket!")
		self.price = round(default_price*0.6, 2)
		self.type_of_ticket = "Early"
		self.id = uuid.uuid4()

class Studentticket(Ticket):
	def __init__(self):
		super().__init__(default_price, days_before)
		self.price = round(default_price*0.5, 2)
		self.type_of_ticket = "Student"
		self.id = uuid.uuid4()

class Lateticket(Ticket):
	def __init__(self):
		super().__init__(default_price, days_before)
		if days_before >=10:
			raise ValueError("Unreal create Lateticket!")
		self.price = round(default_price*1.1, 2)
		self.type_of_ticket = "Late"
		self.id = uuid.uuid4()

firstticket = Studentticket()
secondticket = Lateticket()
firstticket.create_ticket('as23ds3d-dss5-sd6f-sd22-fgdhsj3i3ns7')
print(firstticket.get_info('as23ds3d-dss5-sd6f-sd22-fgdhsj3i3ns7'))
print(firstticket)
print(secondticket)
