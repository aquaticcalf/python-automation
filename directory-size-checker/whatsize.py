import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_directory_size(dp)
    return total_size

directory_path = input("Enter the path of the directory: ")
print(f"Total size of '{directory_path}' is: {get_directory_size(directory_path)} bytes")