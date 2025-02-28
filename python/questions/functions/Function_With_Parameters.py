
# Function With Parameters
def greet(name):
    print("Hello,", name)


# Function Without Parameters
def greet2():
    print("Hello, World!")

greet("Ali")   # Passing an argument
greet("karan")
greet2()

#Return Statement

def add(a, b):
    return a + b  # Returns the sum

result = add(10, 5)
print("Sum:", result)


# Default Parameters

def greet(name="Guest"):
    print("Hello,", name)

greet()          # Uses default value "Guest"
greet("Ali")  # Uses provided argument

# Keyword Arguments

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=21, name="Ali")  # Arguments out of order
