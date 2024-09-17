import csv
class Item:
    pay_rate = 0.8 # the pay rate after 20% discount

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
    
    @classmethod    
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader =  csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )

    @staticmethod
    def is_inetger(num):
        # isinstance check if the argument is of a datatype, in this case, float
        if isinstance(num, float):
            # count out the float that are point zero 
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"
         

# Item.instantiate_from_csv()
# print(Item.all)
print(Item.is_inetger(7.6))