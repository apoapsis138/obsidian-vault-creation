import os
import re
import sys


# Validate Vault Name
# Added some error handling for input validation
# Wondering if, instead of taking this as a user input once the program is launched
#   if it might not be better to take it as a sys.argv, perform the validation
def get_valid_vault(path, vault):
    while True:
        pattern = r"([<>:\"/\\\|?\*\.])"
        invalid_characters = "<>:\"/\\|?*.\""
        if re.search(pattern, vault):
            print(f"Invalid Vault name. You cannot create a vault that contain these characters {invalid_characters}.")
            break
        elif os.path.isdir(os.path.join(path, vault)):
            print(f"Vault {vault} already exists. Please choose a new name.")
            break
        else:
            return vault


# Function to create the folder and file structure
def create_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, f"{file}.md")
            if os.path.exists(file_path):
                print(f"The note {file}.md already exists")
                continue
            try:
                with open(file_path, 'w') as note:
                    note.write(f"# {file}\n")
            except IOError as error:
                print(f"An error occurred while creating the note '{file}.md: {error}")


# Takes sys.argvs now - may want to consider a default value for 'path' - maybe the cwd or a user-defined variable
def main(path, vault):

    # Define Vault name
    valid_vault = get_valid_vault(path, vault)

    # Get the path where the new vault will live
    base_path = os.path.join(path, valid_vault)

    # Defines the folder structure and initial notes of the vault using a dictionary
    # Key is the name of the folder to be created, list of values are the initial notes to create
    # TO-DO: Support nested directories
    # TO-DO: Support using file (maybe json?) to define structure
    # Alternatively, take user input for each folder and note
    structure = {
        'Basics': ['Introduction to Python', 'Variables and Data Types', 'Control Flow'],
        'Data Structures': ['Lists', 'Dictionaries', 'Tuples and Sets'],
        'Functions and Modules': ['Functions', 'Lambda Functions', 'Modules and Packages'],
        'OOP': [],
        'Libraries': [],
        'Web Development': ['Flask', 'Django'],
        'Scripting and Automation': [],
        'Data Analysis': [],
        'Machine Learning': [],
        'Regular Expressions': [],
        'Project Notes': [],
        'Resources': ['Tutorials', 'Documentation', 'Books', 'Online Courses']
    }

    create_structure(base_path, structure)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <filepath> <vault_name>")
        sys.exit(1)

    obsidian_path = sys.argv[1]
    vault_name = sys.argv[2]
    main(obsidian_path, vault_name)