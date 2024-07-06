def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

# Factorial using recursion
print(fact(6))

# Nth - Fibonacci using recursion.

def Fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return Fib(n-1)+Fib(n-2)

print(Fib(5))

