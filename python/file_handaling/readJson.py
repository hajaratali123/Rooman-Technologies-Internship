import json
import os

# File Name
FILE_NAME = "data.json"

# Sample Data
sample_data = {
    "name": "Ali",
    "age": 21,
    "city": "Bangalore",
    "skills": ["Python", "Java", "MERN"]
}

# Function to write data to a JSON file
def write_json(data, filename=FILE_NAME):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("✅ Data written to JSON file successfully!")

# Function to read data from a JSON file
def read_json(filename=FILE_NAME):
    if not os.path.exists(filename):  # Check if file exists
        print("❌ File not found!")
        return None
    with open(filename, "r") as file:
        data = json.load(file)
    print("📖 Data read successfully!\n", data)
    return data

# Function to append new data (without deleting existing content)
def append_json(new_data, filename=FILE_NAME):
    data = read_json(filename)
    if data is None:
        data = {}  # If file doesn't exist, create a new dict
    data.update(new_data)  # Merge new data
    write_json(data, filename)
    print("✅ Data appended successfully!")

# Function to write a list of dictionaries (for multiple records)
def write_list_json(data_list, filename="students.json"):
    with open(filename, "w") as file:
        json.dump(data_list, file, indent=4)
    print("✅ List of data written successfully!")

# Function to read a list of JSON objects
def read_list_json(filename="students.json"):
    if not os.path.exists(filename):
        print("❌ File not found!")
        return
    with open(filename, "r") as file:
        data_list = json.load(file)
    print("\n📖 Student Records:")
    for student in data_list:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# ----------------------------- #
# 🚀 Main Program Execution
# ----------------------------- #

# Write sample data
write_json(sample_data)

# Read and display data
read_json()

# Append new data
new_data = {"email": "ali@example.com", "phone": "9876543210"}
append_json(new_data)

# Work with a list of student records
students = [
    {"name": "Ali", "age": 21, "grade": "A"},
    {"name": "Sara", "age": 20, "grade": "B"},
    {"name": "John", "age": 22, "grade": "A+"}
]
write_list_json(students)
read_list_json()
