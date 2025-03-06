# Program: Demonstration of Various Python Errors and Exception Handling

# Custom Exception class
class MyCustomError(Exception):
    """Custom exception for demonstration purposes."""
    pass

def demonstrate_name_error():
    # NameError occurs when trying to access a variable that hasn't been defined.
    try:
        print(undefined_variable)  # undefined_variable is not defined
    except NameError as e:
        print("Caught a NameError:", e)

def demonstrate_type_error():
    # TypeError occurs when an operation is applied to an object of inappropriate type.
    try:
        result = "Hello" + 5  # Cannot concatenate a string with an integer
    except TypeError as e:
        print("Caught a TypeError:", e)

def demonstrate_value_error():
    # ValueError occurs when a function receives an argument with the right type but an inappropriate value.
    try:
        number = int("abc")  # "abc" cannot be converted to an integer
    except ValueError as e:
        print("Caught a ValueError:", e)

def demonstrate_index_error():
    # IndexError occurs when accessing a sequence with an index that is out of range.
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Index 5 is out of range for this list
    except IndexError as e:
        print("Caught an IndexError:", e)

def demonstrate_key_error():
    # KeyError occurs when trying to access a dictionary with a key that doesn't exist.
    try:
        my_dict = {"a": 1, "b": 2}
        print(my_dict["c"])  # "c" is not a key in my_dict
    except KeyError as e:
        print("Caught a KeyError:", e)

def demonstrate_zero_division_error():
    # ZeroDivisionError occurs when dividing by zero.
    try:
        result = 10 / 0  # Division by zero is not allowed
    except ZeroDivisionError as e:
        print("Caught a ZeroDivisionError:", e)

def demonstrate_attribute_error():
    # AttributeError occurs when a variable does not have a specified attribute.
    try:
        number = 10
        number.append(5)  # 'int' object has no attribute 'append'
    except AttributeError as e:
        print("Caught an AttributeError:", e)

def demonstrate_import_error():
    # ImportError occurs when a module cannot be found.
    try:
        import non_existent_module  # This module does not exist
    except ImportError as e:
        print("Caught an ImportError:", e)

def demonstrate_custom_exception():
    # Demonstrate raising and handling a custom exception.
    try:
        raise MyCustomError("This is a custom error message!")
    except MyCustomError as e:
        print("Caught MyCustomError:", e)

def main():
    print("Demonstrating various Python errors and exceptions with proper handling:\n")
    
    demonstrate_name_error()
    demonstrate_type_error()
    demonstrate_value_error()
    demonstrate_index_error()
    demonstrate_key_error()
    demonstrate_zero_division_error()
    demonstrate_attribute_error()
    demonstrate_import_error()
    demonstrate_custom_exception()

if __name__ == "__main__":
    main()
