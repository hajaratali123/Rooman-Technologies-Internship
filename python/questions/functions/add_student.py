def add_student():
    global total_students
    total_students += 1
    print(f"Student added. Total students: {total_students}")

def process_fees(students):
    total_fees = 0
    for student in students:
        total_fees += student['fees']
    print(f"Total fees collected: {total_fees}")

# Initialize student count
total_students = 0

# Add students
add_student()
add_student()

# Define student records with fees
students = [
    {"name": "Ali", "fees": 5000},
    {"name": "Sara", "fees": 4500}
]

# Process student fees
process_fees(students)
