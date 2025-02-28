
# 1. Function Overloading (Same Function, Different Parameters)
# Function overloading allows multiple functions with the same name but different arguments. 
# However, Python does not support function overloading natively 
# (like Java or C++). Instead, we can achieve it using default arguments or *args and **kwargs.

class MathOperations:
    def add(self, a, b=0, c=0):  # Default values handle multiple cases
        return a + b + c

math_obj = MathOperations()
print(math_obj.add(5))       # Output: 5
print(math_obj.add(5, 10))   # Output: 15
print(math_obj.add(5, 10, 15)) # Output: 30



# Example 2: Function Overloading using *args
# We can also use *args to accept a variable number of arguments.


class MathOperations:
    def add(self, *args):  # Accepts any number of arguments
        return sum(args)

math_obj = MathOperations()
print(math_obj.add(5))          # Output: 5
print(math_obj.add(5, 10))      # Output: 15
print(math_obj.add(5, 10, 15))  # Output: 30


# 2. Function Overriding (Same Function, Different Behavior in Child Class)
# Function overriding occurs when a child class provides a different implementation for a method already defined in the parent class.

# Example: Overriding in Python


class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):  # Overriding the parent method
        print("This is the Child class.")

# Creating objects
parent_obj = Parent()
child_obj = Child()

parent_obj.show()  # Output: This is the Parent class.
child_obj.show()   # Output: This is the Child class.


# 3. Using super() to Call Parent Method
# If you want to use both the parent and child method, use super():

class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):
        super().show()  # Calls the parent method
        print("This is the Child class.")

child_obj = Child()
child_obj.show()
