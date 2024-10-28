# Lets explore more on constructor.
# Lets add constrain on the type of data recieved by constructor and lets validate the data.

class Item:
    def __init__(self,name , quantity , price):
        
        # Validating the arguments.
        assert quantity >= 0 , "Quantity is not greater than 0"
        assert price >= 0 , "Price is not greater than 0"

        # Initialisation of Object
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def Total_cost(self):
        return self.price * self.quantity

Item1 = Item("Pen" , -1 , 5)
print(Item1.Total_cost())