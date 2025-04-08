"""
Here's what's happening:

1. fibonacci(n) calls fibonacci(n-1) and fibonacci(n-2)
2. fibonacci(n-1) calls fibonacci((n-1)-1) and fibonacci((n-1)-2)
3. fibonacci(n-2) calls fibonacci((n-2)-1) and fibonacci((n-2)-2)

And so on, until we reach the base cases (n == 1 or n == 2).

Example Walkthrough
Let's say we call fibonacci(4):

1. fibonacci(4) calls fibonacci(3) and fibonacci(2)
2. fibonacci(3) calls fibonacci(2) and fibonacci(1)
3. fibonacci(2) returns 1 (base case)
4. fibonacci(1) returns 0 (base case)
5. fibonacci(3) returns fibonacci(2) + fibonacci(1) = 1 + 0 = 1
6. fibonacci(4) returns fibonacci(3) + fibonacci(2) = 1 + 1 = 2
"""

"""
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 13
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
"""

# n = 10
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b




# n = 10
# a, b = 0, 1
# for i in range(n):
#     a, b = b, a + b
# print(a)

def f(n):
    if n <= 1:
        return n
    else:
        return f(n - 1) + f(n - 2)

print(f(19))
