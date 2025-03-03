def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

# Dictionary acting as a switch
operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1/2/3/4): "))

if choice in operations:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = operations[choice](num1, num2)  # Calls the corresponding function
    print("Result:", result)
else:
    print("Invalid choice! Please select a valid option.")
