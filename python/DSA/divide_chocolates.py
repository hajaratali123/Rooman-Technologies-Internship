def divide_chocolates():
    chocolates = 10  # Total chocolates

    try:
        students = int(input("Enter the number of students: "))  # Get user input
        if students <= 0:
            raise ValueError("The number of students must be greater than zero.")

        chocolates_per_student = chocolates / students  # Divide chocolates
        print(f"Each student gets {chocolates_per_student} chocolates.")

    except ZeroDivisionError:
        print("Error: Cannot divide chocolates among zero students. Please enter a valid number.")
    except ValueError as e:
        print(f"Invalid input: {e}")  # Handles non-numeric and invalid values

# Run the function
divide_chocolates()


def cal_markes(total_makes,optain_markse):
     res = optain_markse/total_makes

def stundet():
    student = input("Enter your name: ")
    roll_number = input("Enter the roll number :")
    total_makes = input("Enter the total marks:")
    optain_markse = input("Enter the optain marks:")
    cal_markes(total_makes,optain_markse)


def main():
    print(stundet())
   
    