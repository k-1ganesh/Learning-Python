# Lets create Function within the class and use it.

class Item:
    def total_price(self , EachPrice, Totalquantity):
        return EachPrice * Totalquantity

# Self : Whenever any method is created inside the class it always has self as one of its argument.
# Whenever any object calls method of class that object is passed as an argument to that method which is received in self variable. 
# Name of self can be changed it all about convention. 
# Position of self can't be changed.
# Self must be the first parameter.
# self refers to the specific instance of the class you are working with.


Item1 = Item()
Item1.name = "Spoon"
Item1.quantity = 100
Item1.price = 10
Cost = Item1.total_price(Item1.price , Item1.quantity)
print(Cost)

Item2 = Item()
Item1.name = "Phone"
Item1.quantity = 10
Item1.price = 10000
Cost = Item1.total_price(Item1.price , Item1.quantity)
print(Cost)