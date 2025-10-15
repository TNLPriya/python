import os

# 1. Define custom exception
class EmptyFileError(Exception):
    pass

filename = input("Enter the filename: ")

file = None
try:
    # 3. Try opening the file
    file = open(filename, "r")

    # 4. Check if file is empty
    if os.path.getsize(filename) == 0:
        raise EmptyFileError("The file is empty.")

    # 5. Read and process content
    content = file.read()
    words = content.split()
    print(f"The file has {len(words)} words.")

# 6. Handle exceptions
except FileNotFoundError:
    print("Error: The specified file was not found.")
except EmptyFileError as e:
    print(f"Error: {e}")

# 7. Finally block
finally:
    if file:
        file.close()
    print("File operation completed")
