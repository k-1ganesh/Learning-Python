# IN this type of inheritance child class inherit from only one parent class.

class Animal:
    def sound(self):
        print("Animal Makes some sound")

class Dog(Animal):
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def sound(self):
        print("Bhoo Bhoo")

Dog1 = Dog("Rocky","Golden Retriever")
Dog1.sound()