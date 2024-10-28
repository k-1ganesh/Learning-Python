# Lets learn How to define class and how to create its instace / object

class Item:
    pass   # This is used when we want to have empty class . Otherwise class must have something into it

obj1 = Item() # In this way object are created.

print(type(obj1)) # This gives an idea that obj1 is instance of class Item. 

obj1.name = "Spoon"
obj1.color = "Red" # now this attributes are not defined in Item class So this attributes are specific to obj1 only. 

