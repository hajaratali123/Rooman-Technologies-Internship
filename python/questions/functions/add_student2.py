def add_student():
    global total_students
    total_students += 1
    print(f"Student added. Total students: {total_students}")

def process_fees(students):
    total_fees = sum(student['fees'] for student in students)
    print(f"Total fees collected: {total_fees}")

def display_info(student):
    print("\n Student Information:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Fees: {student['fees']}")
        print("Marks:")
        for subject, score in student['marks'].items():
            print(f"{subject}: {score}")

# Initialize student count
total_students = 0

# Get number of students
num_students = int(input("Enter the number of students: "))

# List to store student data
students = []

# Taking student details as input
for _ in range(num_students):
    name = input("Enter student name: ")
    fees = float(input(f"Enter fees for {name}: "))
    num_subjects = int(input(f"Enter the number of subjects for {name}: "))
    marks={}

    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        score = float(input(f"Enter mark for {subject}: "))
        marks[subject] = score
    students.append({"name": name, "fees": fees,"marks":marks})
    add_student()

# Process fees
process_fees(students)

display_info(students)
