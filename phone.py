from items import Item

class Phone(Item): # chilc class
    all = []
    def __init__(self, name: str, price: float, quantity=10, broken_phones=0):

        # call the instances from the parent class
        super().__init__(
            name, price, quantity
        )
        # Run Validation of recieved arguments
        assert broken_phones >=0, f"broken_phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.broken_phones = broken_phones
        
        Phone.all.append(self)