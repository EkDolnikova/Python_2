import os

def get_file_info(file_path):
    filepath, file_extension = os.path.splitext(file_path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)

print(get_file_info(file_path = 'file_in_current_directory.txt'))