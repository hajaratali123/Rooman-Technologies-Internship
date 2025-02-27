name = "Ali"
if name == "Ali":
    print("Welcome, Ali!")  # Indentation is required


# Declaring Variables

print("Declaring Variables")
name = "Ali"   # String
age = 21       # Integer
height = 5.9   # Float
is_student = True  # Boolean

#Checking Data Type
print("Checking Data Type")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


#Data Types in Python
print("Data Types in Python")


#Operators and Expressions
print("Operators and Expressions")
a = 10
b = 3

print(a + b)  # 13 (Addition)
print(a - b)  # 7  (Subtraction)
print(a * b)  # 30 (Multiplication)
print(a / b)  # 3.33 (Division)
print(a // b) # 3 (Floor Division, removes decimal)
print(a % b)  # 1 (Modulus, remainder)
print(a ** b) # 1000 (Exponentiation, 10³)

#Comparison Operators
print("Comparison Operators")

a = 10
b = 5

print(a > b)  # True
print(a < b)  # False
print(a == b) # False
print(a != b) # True
print(a >= b) # True
print(a <= b) # False


#Logical Operators
print("Logical Operators")
x = True
y = False

print(x and y) # False (Both must be True)
print(x or y)  # True (At least one is True)
print(not x)   # False (Negation)
print(not y)   # True (Negation)

#Bitwise Operators
print("Bitwise Operators")
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1  (Bitwise AND -> 0001)
print(a | b)  # 7  (Bitwise OR -> 0111)
print(a ^ b)  # 6  (Bitwise XOR -> 0110)
print(~a)     # -6 (Bitwise NOT)
print(a << 1) # 10 (Left Shift)
print(a >> 1) # 2  (Right Shift)


# Control Flow (if-else, loops)
#if-else Statements
print("if-else statemets")

age = 20

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


#Loops
print("for Loops")
for i in range(5):  # 0 to 4
    print(i)


#While Loop
print("While Loop")
count = 0
while count < 5:
    print(count)
    count += 1


#Loop Control Statements
print("Loop Control Statements")


for i in range(5):
    if i == 3:
        break  # Stops at 3
    print(i)


for i in range(5):
    if i == 3:
        continue  # Skips 3
    print(i)




#Exception Handling
print("Exception Handling")

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Enter a number.")
finally:
    print("Execution completed.")

