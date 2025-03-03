# 📚 Step 1: Create a dictionary to store student details
students = {
    1: {
        "name": "Ali",
        "age": 20,
        "class": "12th",
        "subjects": {"Math": 95, "Science": 88, "English": 90},
        "grade": "A"
    },
    2: {
        "name": "Sara",
        "age": 19,
        "class": "11th",
        "subjects": {"History": 85, "Geography": 80, "English": 89},
        "grade": "B"
    },
}

# 🎓 Step 2: Display student records
def display_students():
    print("\n📖 Student Records:")
    for key, student in students.items():
        subjects_scores = ", ".join(f"{sub}: {score}" for sub, score in student["subjects"].items())
        print(f"{key}. Name: {student['name']}, Age: {student['age']}, Class: {student['class']}, "
              f"Subjects & Scores: {subjects_scores}, Grade: {student['grade']}")

display_students()

# ✍️ Step 3: Add a new student
new_name = input("\nEnter Student Name: ")
new_age = int(input("Enter Age: "))
new_class = input("Enter Class: ")

# 📌 Enter subjects and scores
new_subjects = {}
while True:
    subject = input("Enter Subject Name (or type 'done' to finish): ")
    if subject.lower() == "done":
        break
    score = int(input(f"Enter Score for {subject}: "))
    new_subjects[subject] = score

# 🎯 Calculate Grade
average_score = sum(new_subjects.values()) / len(new_subjects)
if average_score >= 90:
    new_grade = "A"
elif average_score >= 80:
    new_grade = "B"
elif average_score >= 70:
    new_grade = "C"
elif average_score >= 60:
    new_grade = "D"
else:
    new_grade = "F"

# 🆕 Assign a unique ID
new_id = max(students.keys()) + 1
students[new_id] = {
    "name": new_name,
    "age": new_age,
    "class": new_class,
    "subjects": new_subjects,
    "grade": new_grade,
}

print("\n📚 Updated Student Records:")
display_students()
