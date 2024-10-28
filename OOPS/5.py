# Lets learn about Inheritance.
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def DisplayName(self):
        print(f"Name of employee is {self.name} and Its id is {self.id}")

# emp1 = Employee("Ganesh Kachare" , 1)

# Now lets suppose I want to  create other class which stores other information but also requires information of Employee class. So instead of adding the same information of Employee class on that new class we can simply inherit Employee Class.

class Programmer(Employee):
    def __init__(self,name):
        self.name = name
    def DisplayLanguage(self):
        print("Default Fav language is Python")

Prog1 = Programmer("Tushar Kachare",1 )
Prog1.DisplayLanguage()
Prog1.DisplayName()

### Key Takeaways.
# If Inherited class don't have init method then init method of parent will be executed.
# If It has init method then only that method will be executed.
# If child class has init and still we want to execute init method of parent class then we need to use the super() keyword.