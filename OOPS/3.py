# Lets understand Constructor .
# Constructor is a special function which always run when object of class gets created. 
# Constructor can be used to do initialisation of objects

class Item:
    def __init__(self , name , price , quantity): # This is constructor.
        self.name = name
        self.price = price
        self.quantity = quantity
    def Total_Cost(self):
        return self.price * self.quantity

Item1 = Item('spoon' , 10 , 100)
Item2 = Item("Phone" , 10000, 5)

print(f"Total Cost of Item1 : {Item1.Total_Cost()}")
print(f"Total Cost of Item2 : {Item2.Total_Cost()}")
                