# Understanding public , private , protected.
# Python do not have this kind of concept Everything is public in python.
# But still some conventions are followed by programmers to model the behaviour of private and protected.

# Private -> Can't be accessed from outside of class. Accessed only from within the class.
# Protected -> Can be accessed from withing the class or its childclass.

# Private -> __varName is used in python. (Just Convention)
# Protected -> -varName is used in python (Just Convention)

class Employee:
    def __init__(self,name):
        self.__name = name # Name is private by convention
    def Show_Name(self):
        print(f"Name of Employee is {self.__name}")
emp1 = Employee("Ganesh")
# print(emp1.__name) In Normal way we can't access it so its kind of private. 
# But still we can access it.
print(emp1._Employee__name)        