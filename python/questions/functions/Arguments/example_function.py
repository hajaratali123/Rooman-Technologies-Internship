# How *args and **kwargs Store Arguments in Python
# When we use *args and **kwargs in a function, they collect the arguments in specific data structures:

# *args → Tuple (tuple)
# **kwargs → Dictionary (dict)


def example_function(*args):
    print(args)
    print(type(args))  # Check the data type

example_function(1, 2, 3, "Ali", [4, 5])

def example_function(**kwargs):
    print(kwargs)
    print(type(kwargs))  # Check the data type

example_function(name="Ali", age=21, city="Bangalore")
