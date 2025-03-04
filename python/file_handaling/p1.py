import os

filename = "example.txt"

# Check if the file exists, otherwise create it
if not os.path.exists(filename):
    print(f"File '{filename}' not found. Creating a new file...")
    with open(filename, "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("Python file handling is fun!\n")

# Now try reading the file
with open(filename, "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)


# Get student name from the user
new_student = input("Enter the new student's name: ")

# Open the file in append mode and add the new name
with open("example.txt", "a") as file:
    file.write(new_student + "\n")

print(f"\nNew student '{new_student}' added successfully!")
