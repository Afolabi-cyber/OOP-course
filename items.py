import csv
class Item: #  parent class
    all = []
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity=10):
        # Run Validation of recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        Item.all.append(self)
    @property
    def price(self):
        return self.__price
    
    def apply_increment(self, increment):
        self.__price = self.__price + self.__price * increment

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate 
    
    @property
    def name(self):
        print('You are trying to print name')
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long')
        else:
            self.__name = value


    def calculate_total_price(self):
        return self.__price * self.quantity
    
    
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
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
    
    @property
    def read_only_name(self):
        return 'AAA'
    
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
            
            Hello someone,
            we have {self.name}, {self.quantity} times.
            Regards, Faruq.
    
            """
    def __send():
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
    
