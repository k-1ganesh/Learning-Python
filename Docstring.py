# It gives the description about the function . 
# It needs to just below the function name.

# Note : Docstring is not comment


def square(x):
    '''This function computes the square of input''' 
    return x**2

print(square(5))
print(square.__doc__) 