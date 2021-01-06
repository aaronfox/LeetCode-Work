# Quick Recursion demo for friend. 
# F0 = 1. F1 = 1.
# Fn = F(n-1) + F(n-2)

# Returns nth number from the Fibonacci sequence
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(8))


