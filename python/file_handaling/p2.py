
import os

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
    except FileNotFoundError:
        print(f"\nFile '{filename}' not found! Please create it first.")

# Call function
read_file("attendance.txt")

def add_student(filename):
    new_student = input("\nEnter the new student's name: ")

    with open(filename, "a") as file:
        file.write(new_student + "\n")
    
    print(f"\nStudent '{new_student}' added successfully!")

# Call function
add_student("attendance.txt")




def create_attendance_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Attendance List:\n")
        print(f"\nNew attendance file '{filename}' created!")
    else:
        print(f"\nAttendance file '{filename}' already exists.")

# Call function
create_attendance_file("attendance.txt")

