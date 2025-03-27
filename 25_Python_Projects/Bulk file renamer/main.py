import os
from termcolor import colored

def bulk_rename(directory, condition):
    try:
        files = os.listdir(directory)

        for filename in files:
            old_file_path = os.path.join(directory, filename)

            if os.path.isfile(old_file_path):
                new_filename = condition(filename)
                new_file_path = os.path.join(directory, new_filename)

                os.rename(old_file_path, new_file_path)

                print(colored(f"Renamed: {filename} -> {new_filename}", "green"))
    
    except Exception as e:
        print(colored(f"Error: {e}", "red"))

def condition(filename):
    return 'new_' + filename

if __name__ == "__main__":
    directory = input("Enter the directory path: ")

    bulk_rename(directory, condition)
