import csv

file_path = r"C:\Users\Admin\Desktop\Room_Internship\students.csv"

with open(file_path, mode="r", encoding="latin-1") as file:  # Use latin-1 encoding
    reader = csv.reader(file)
    
    for row in reader:
        print(row)
