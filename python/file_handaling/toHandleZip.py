import zipfile
import os

# Define the ZIP file name
ZIP_FILE_NAME = "my_files.zip"

# Sample files to add
FILE_1 = "file1.txt"
FILE_2 = "file2.txt"

# Function to create sample text files
def create_sample_files():
    with open(FILE_1, "w") as f:
        f.write("Hello, this is File 1.")
    with open(FILE_2, "w") as f:
        f.write("This is File 2 with some content.")
    print("✅ Sample files created!")

# Function to create a ZIP file and add files
def create_zip():
    with zipfile.ZipFile(ZIP_FILE_NAME, "w") as zipf:
        zipf.write(FILE_1)
        zipf.write(FILE_2)
    print(f"✅ ZIP file '{ZIP_FILE_NAME}' created successfully!")

# Function to add files to an existing ZIP file
def add_to_zip(file_name):
    with zipfile.ZipFile(ZIP_FILE_NAME, "a") as zipf:
        zipf.write(file_name)
    print(f"✅ '{file_name}' added to ZIP file!")

# Function to extract ZIP contents
def extract_zip(destination_folder="extracted_files"):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    with zipfile.ZipFile(ZIP_FILE_NAME, "r") as zipf:
        zipf.extractall(destination_folder)
    print(f"✅ ZIP file extracted to '{destination_folder}'!")

# Function to list files inside the ZIP
def list_zip_contents():
    with zipfile.ZipFile(ZIP_FILE_NAME, "r") as zipf:
        file_list = zipf.namelist()
    print("📂 Files inside ZIP:", file_list)

# Function to read a file from ZIP without extracting
def read_file_from_zip(file_name):
    with zipfile.ZipFile(ZIP_FILE_NAME, "r") as zipf:
        with zipf.open(file_name) as file:
            content = file.read().decode()
    print(f"📖 Content of '{file_name}':\n{content}")

# ----------------------------- #
# 🚀 Main Program Execution
# ----------------------------- #

create_sample_files()  # Create files
create_zip()           # Create ZIP
list_zip_contents()    # List files in ZIP
extract_zip()          # Extract ZIP
read_file_from_zip(FILE_1)  # Read file from ZIP
