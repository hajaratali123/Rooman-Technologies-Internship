# File Handling in Python

import os

# 1. Creating and Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, this is a new file.\n")
    file.write("This is the second line.\n")
print("File 'example.txt' created and written successfully.")

# 2. Reading the File
with open("example.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)

# 3. Appending to the File
with open("example.txt", "a") as file:
    file.write("This line is added using append mode.\n")
print("\nNew content appended successfully.")

# 4. Reading File Line by Line
with open("example.txt", "r") as file:
    print("\n--- Reading Line by Line ---")
    for line in file:
        print(line.strip())  # Removing extra spaces

# 5. Checking if a File Exists
if os.path.exists("example.txt"):
    print("\nFile 'example.txt' exists.")
else:
    print("\nFile does not exist.")

# 6. Renaming the File
os.rename("example.txt", "new_example.txt")
print("\nFile renamed to 'new_example.txt'.")

# 7. Checking File Size
file_size = os.path.getsize("new_example.txt")
print(f"\nFile Size: {file_size} bytes")

# 8. Copying File Content (Simulating Copy)
with open("new_example.txt", "r") as source, open("copy_example.txt", "w") as dest:
    dest.write(source.read())
print("\nFile copied to 'copy_example.txt'.")

# 9. Creating and Removing a Directory
os.mkdir("test_folder")
print("\nFolder 'test_folder' created.")

if os.path.exists("test_folder"):
    os.rmdir("test_folder")
    print("\nFolder 'test_folder' removed.")

# 10. Deleting a File
if os.path.exists("new_example.txt"):
    os.remove("new_example.txt")
    print("\nFile 'new_example.txt' deleted.")

if os.path.exists("copy_example.txt"):
    os.remove("w.txt")
    print("\nFile 'copy_example.txt' deleted.")
