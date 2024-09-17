# When to use class methods and when to use static methods
import csv

class Item: #  parent class
    all = []
    def __init__(self, name: str, price: float, quantity=10):
        # Run Validation of recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate 

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
    # @staticmethod
    # def is_integer(num):
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance 
        '''

    # @classmethod
    # def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship
        with the class, but ussually those are used to 
        '''
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

class Phone(Item): # chilc class
    all = []
    def __init__(self, name: str, price: float, quantity=10, broken_phones=0):

        # call the instances from the parent class
        super().__init__(
            name, price, quantity
        )
        # Run Validation of recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero"
        assert broken_phones >=0, f"broken_phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.broken_phones = broken_phones
        
        Phone.all.append(self)


# no reason to call static or class method from instance level
phone1 = Phone('nokia', 500, 5)
# print(phone1.calculate_total_price())
# phone2 = Phone('Samsung', 700, 5)
print(Item.all)
print(Phone.all)

