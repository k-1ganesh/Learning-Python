# Its like Switch Case of C++
x = int(input("Enter the number: "))
match x:
    case 0:
        print("X is 0")
    case 1:
        print("X is 1")
    case _: # Default Case
        print("X is neither 0 nor 1")        


