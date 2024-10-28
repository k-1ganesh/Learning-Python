# In this A -> B -> C happens.

class Human:
    def Walk(self):
        print("Yes He can walk")
    def Talk(self):
        print("Yes He can talk")
    def Think(self):
        print("Yes He can think")

class Employee(Human):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def Work(self):
        print("Employee do work")

class Programmer(Employee):
    def Write_Program(self):
        print("Yes do write programs")
    def showname(self):
        print(self.name)

p1 = Programmer("Ganesh" , 28)
p1.showname()
p1.Work()
p1.Think()