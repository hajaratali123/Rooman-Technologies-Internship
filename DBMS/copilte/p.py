 # write a progrma add two numbers 


# Program to add two numbers using a switch-like structure

def add_numbers(a, b):
    return a + b

def switch_case(operation, a, b):
    switch = {
        "add": add_numbers
    }
    # Get the function based on the operation, default to None if not found
    func = switch.get(operation, None)
    if func:
        return func(a, b)
    else:
        return "Invalid operation"

# Example usage
num1 = 5
num2 = 10
operation = "add"  # You can change this to test other cases
result = switch_case(operation, num1, num2)
print(f"Result: {result}")