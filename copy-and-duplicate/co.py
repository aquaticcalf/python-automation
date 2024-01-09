import os

def copy_and_rename(src_path, num_copies):

    if not os.path.exists(src_path):
        print(f"shut up grandpa, stop making stuff up, there is no file at {src_path}")
        return

    src_dir, src_filename = os.path.split(src_path)

    name, file_extension = os.path.splitext(src_filename)

    for i in range(1, num_copies + 1):

        new_filename = f"{name}-{i:04d}{file_extension}"

        dest_path = os.path.join(src_dir, new_filename)

        os.system(f"cp \"{src_path}\" \"{dest_path}\"")

        print(f"file {new_filename} copied")

if __name__ == "__main__":
    src_path = input("path to the source file: ")
    num_copies = int(input("number of copies you need: "))

    copy_and_rename(src_path, num_copies)
