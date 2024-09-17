from items import Item
from phone import Phone
from keyboard import Keyboard

#Item.instantiate_from_csv()
item1 = Keyboard('MyKeyboard', 750)
# item1.name = 'otheritem' # read only attributes cannot be reasigned

#using the name.setter decorator, which isnt a read-only.
# item1.name = 'OtherItem'
# item1.__price = 900
# print(item1.price)
# print('increment')
# item1.apply_increment(.1)

print(item1.apply_discount())
print(item1.price)

# item1.send_email()

# Read only property can be accesed using the property decorator, they cannot be renamed