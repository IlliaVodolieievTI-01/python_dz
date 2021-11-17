import uuid
import json

id_length = 36
earlyday = 60
earlycoef = 0.6
studentcoef = 0.5
lateday = 10
latecoef = 1.1
roundcoef = 2

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
        self.data_id['ticket'] = {}
        with open('data.json', 'w') as f:
            json.dump(self.data_id, f, indent=4)

    def create_ticket(self, id):
        with open('data.json', 'r') as f1:
            self.data_id = json.load(f1)
        if not len(str(id)) == id_length:
            raise TypeError("Id must be have 36 symbols!")
        self.id = id
        self.data_id['ticket'][str(self.id)] = {}
        self.data_id['ticket'][str(self.id)]['type'] = self.type_of_ticket
        self.data_id['ticket'][str(self.id)]['days'] = self.days
        self.data_id['ticket'][str(self.id)]['price'] = self.price
        with open('data.json', 'w') as f1:
            json.dump(self.data_id, f1, indent=4)

    def get_info(self, value_id):
        with open('data.json') as f2:
            self.data_id = json.load(f2)
        if value_id not in self.data_id['ticket']:
            raise ValueError("Not found this id!")
        for id in self.data_id['ticket'].keys():
            if value_id == id:
                return f"{value_id} --- {str(self.data_id['ticket'][value_id])}"

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
        if days_before < earlyday:
            raise ValueError("Unreal create Earlyticket!")
        self.price = round(default_price * earlycoef, roundcoef)
        self.type_of_ticket = "Early"
        self.id = uuid.uuid4()


class Studentticket(Ticket):
    def __init__(self):
        super().__init__(default_price, days_before)
        self.price = round(default_price * studentcoef, roundcoef)
        self.type_of_ticket = "Student"
        self.id = uuid.uuid4()


class Lateticket(Ticket):
    def __init__(self):
        super().__init__(default_price, days_before)
        if days_before >= lateday:
            raise ValueError("Unreal create Lateticket!")
        self.price = round(default_price * latecoef, roundcoef)
        self.type_of_ticket = "Late"
        self.id = uuid.uuid4()


firstticket = Studentticket()
secondticket = Lateticket()
thirdticket = Studentticket()
firstticket.create_ticket('as23ds3d-dss5-sd6f-sd22-fgdhsj3i3ns7')
thirdticket.create_ticket('we23ds3d-dss5-sd6f-sd22-fgdhsj3i3ns7')
print(firstticket.get_info('as23ds3d-dss5-sd6f-sd22-fgdhsj3i3ns7'))
print(thirdticket.get_info('we23ds3d-dss5-sd6f-sd22-fgdhsj3i3ns7'))
print(firstticket)
print(secondticket)