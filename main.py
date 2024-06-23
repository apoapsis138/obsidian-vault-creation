import os
import re


# Validate Vault Name
# Added some error handling for input validation
# Wondering if, instead of taking this as a user input once the program is launched
#   if it might not be better to take it as a sys.argv, perform the validation
def get_valid_vault(obsidian_directory):
    while True:
        pattern = r"([<>:\"/\\\|?\*\.])"
        invalid_characters = "<>:\"/\\|?*.\""
        valid_name = input("Enter the name of your new Obsidian vault: ")
        if re.search(pattern, valid_name):
            print(f"Invalid Vault name. You must avoid using the following characters {invalid_characters}.")
        elif os.path.isdir(os.path.join(obsidian_directory, valid_name)):
            print(f"Vault {valid_name} already exists. Please input a new Vault name.")
        else:
            return valid_name


# Function to create the folder and file structure
# TO-DO: Check to see if note already exists, and if so, behavior? (overwrite, append, skip?)
def create_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, f"{file}.md")
            with open(file_path, 'w') as note:
                note.write(f"# {file}\n")


def main():
    # Parent directory for Obsidian Vaults
    # TO-DO: Take this as a sys.argv
    obsidian_directory = "C:\\Users\\nonli\\OneDrive\\Documents\\Obsidian Vaults"

    # Define Vault name
    vault_name = get_valid_vault(obsidian_directory)

    # Get the path where the new vault will live
    base_path = os.path.join(obsidian_directory, vault_name)

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


main()
