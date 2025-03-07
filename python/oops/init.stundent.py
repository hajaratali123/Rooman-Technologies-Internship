class Student:
    def __init__(self, name, roll_number, total_marks, optain_marks,grade):
        self.name = name
        self.roll_number = roll_number
        self.total_marks = total_marks
        self.optain_marks = optain_marks
        self.grade = grade

    def display_stundet(self):
        print(f"Name: {self.name}") 
        print(f"Roll Number: {self.roll_number}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Optain Marks: {self.optain_marks}")
        print(f"Grade: {self.grade}")
        print("\n")

    def Write_stundet(self):
        self.name = input("Enter the name: ")   
        self.roll_number = input("Enter the roll number: ")
        self.total_marks = input("Enter the total marks: ")
        self.optain_marks = input("Enter the optain marks: ")
        self.grade = input("Enter the grade: ")

if __name__ == "__main__":

    Student_obj = Student("Ali", 1, 100, 90, "A")
    Student_obj.display_stundet()
    Student_obj.Write_stundet()
    Student_obj.display_stundet()

