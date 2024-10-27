# Operator Overloading : It is used to change the default behaviour of operators. 
# Used to add the custom behabiors to the operator.

class Vector:
    def __init__(self, i, j , k):
        self.i = i
        self.j = j 
        self.k = k
    def __add__(self1,self2): # This is used to change the behaviour of + 
        print(f"Vector Addition of {self1.i}i+{self1.j}j+{self1.k}k and {self2.i}i+{self2.j}j+{self2.k}k : {self1.i + self2.i}i+{self1.j + self2.j}j+{self1.k + self2.k}k")

v1 = Vector(2 ,3 ,4)
v2 = Vector(5, 6, 3)

Vector.__add__(v1 , v2)