import os

def create_and_write_file(filename):
    """Creates (or overwrites) a file and writes user input to it."""
    data = input("Enter text to write to the file: ")
    # Open the file for writing: create if not exists, truncate if exists
    fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
    try:
        os.write(fd, data.encode())
        print(f"Data has been written to {filename}.")
    finally:
        os.close(fd)

def read_file(filename):
    """Reads and displays the contents of a file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return
    fd = os.open(filename, os.O_RDONLY)
    try:
        file_stat = os.fstat(fd)
        file_size = file_stat.st_size
        # Read the entire file content
        content = os.read(fd, file_size)
        print("File contents:")
        print(content.decode())
    finally:
        os.close(fd)

def delete_file(filename):
    """Deletes the specified file."""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"'{filename}' has been deleted.")
    else:
        print(f"File '{filename}' does not exist.")

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Create and write to a file")
        print("2. Read from a file")
        print("3. Delete a file")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        # Using match-case as a switch-case alternative
        match choice:
            case "1":
                filename = input("Enter file name to create/write: ")
                create_and_write_file(filename)
            case "2":
                filename = input("Enter file name to read: ")
                read_file(filename)
            case "3":
                filename = input("Enter file name to delete: ")
                delete_file(filename)
            case "4":
                print("Exiting program.")
                break
            case _:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
