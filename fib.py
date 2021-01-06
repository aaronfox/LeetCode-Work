# Quick Recursion demo for friend. 
# F0 = 1. F1 = 1.
# Fn = F(n-1) + F(n-2)

# Returns nth number from the Fibonacci sequence using recursion
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Iterative fibonacci using a stack
def iterative_fib(num):
    stack = [num]

    value = 0
    while len(stack) > 0:
        n = stack.pop()
        if n == 0:
            pass
        elif n == 1:
            value = value + 1
        else:
            stack.append(n-1)
            stack.append(n-2)

    return value

print(fib(8))
print(iterative_fib(5))



