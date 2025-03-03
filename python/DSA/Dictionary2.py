# Creating a Dictionary
student = {
    "name": "Ali",
    "age": 22,
    "course": "Computer Science",
    "marks": 85
}

print("Student Dictionary:", student)

# Accessing Values using Keys
print("Name:", student["name"])  # Output: Ali
print("Age:", student.get("age"))  # Using .get() to avoid KeyError


# Adding a New Key-Value Pair
student["city"] = "Bangalore"

# Updating an Existing Key
student["marks"] = 90

print("Updated Dictionary:", student)


# Removing a Specific Key
del student["age"]

# Removing and Returning a Value
removed_value = student.pop("marks")
print("Removed Marks:", removed_value)

# Removing the Last Inserted Key-Value Pair
student.popitem()

print("Dictionary after Deletion:", student)


# Iterating Over Keys
for key in student:
    print("Key:", key)

# Iterating Over Values
for value in student.values():
    print("Value:", value)

# Iterating Over Key-Value Pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Creating a Dictionary with Squared Values
squares = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares)


students = {
    "Ali": {"age": 22, "marks": 85},
    "Sam": {"age": 21, "marks": 92},
}

print("Ali's Marks:", students["Ali"]["marks"])

