def copy_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, 'r') as original_file:
                original_content = original_file.read()
                copy_file_path = file_path.split('.')[0] + '_copy.' + file_path.split('.')[1]
                with open(copy_file_path, 'w') as copy_file:
                    copy_file.write(original_content)
                print(f"Contents copied from {file_path} to {copy_file_path} successfully.")
        else:
            print(f"Error: File '{file_path}' not found.")
import os
file_list = ['file1.txt', 'file2.txt', 'file3.txt']  # List of file paths
copy_files(file_list)
