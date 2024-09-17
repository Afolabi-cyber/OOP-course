from items import Item

class Keyboard(Item): # chilc class
    all = []
    def __init__(self, name: str, price: float, quantity=10):

        # call the instances from the parent class
        super().__init__(
            name, price, quantity
        )