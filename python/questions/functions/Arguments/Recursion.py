# What is Recursion?
# Recursion is a programming technique where a function calls itself to solve a problem. It breaks down a complex problem into smaller subproblems until a base condition is met.

# Basic Structure of a Recursive Function
# A recursive function typically consists of:

# Base Case → The stopping condition to prevent infinite recursion.
# Recursive Case → The function calls itself with a smaller problem.

def factorial(n):
    if n == 0 or n == 1:  # Base Case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive Case

print(factorial(5))  # Output: 120


def fibonacci(n):
    if n == 0:  # Base Case
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive Case

print(fibonacci(6))  # Output: 8


def reverse_string(s):
    if len(s) == 0:  # Base Case
        return s
    else:
        return s[-1] + reverse_string(s[:-1])  # Recursive Case

print(reverse_string("hello"))  # Output: "olleh"

def sum_of_digits(n):
    if n == 0:  # Base Case
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)  # Recursive Case

print(sum_of_digits(1234))  # Output: 10

def print_numbers(n):
    if n == 0:  # Base Case
        return
    print(n)  # Print current number
    print_numbers(n - 1)  # Recursive Call

print_numbers(5)






# Advantages of Recursion
# ✅ Simplifies Complex Problems → Breaks them into smaller, manageable subproblems.
# ✅ Elegant Code → Reduces the need for loops.

# Disadvantages of Recursion
# ❌ High Memory Usage → Each function call is stored in the call stack, which may lead to a stack overflow if recursion depth is too high.
# ❌ Slower Execution → Compared to iteration, recursion can be slower due to function call overhead.

# When to Use Recursion?
# ✔️ Tree or Graph Traversal (like DFS)
# ✔️ Divide and Conquer Algorithms (like Merge Sort, Quick Sort)
# ✔️ Mathematical Problems (like Factorial, Fibonacci, Sum of Digits)