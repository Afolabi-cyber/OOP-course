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

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"
         
item1 = Item("Phone", 100)
#print(item1.apply_discount())
#print(item1.price)

item2 = Item("Laptop", 1000)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
item3 = Item("watch", 500)
item4 = Item("clothe", 700)
item5 = Item("speaker", 800)

# for instance in Item.all:
#     print(instance.quantity)
print(Item.all)

#print(Item.__dict__) # class level attribuites
#print(item1.__dict__) # instance level attributes
