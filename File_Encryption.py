from cryptography.fernet import Fernet
import os  # Added import for handling file existence

# Function to generate and save a Fernet key to a file
def generate_and_save_key():
    key = Fernet.generate_key()
    with open('myKey', 'wb') as myKey:
        myKey.write(key)

# Function to read the Fernet key from a file
def read_key_from_file():
    try:
        with open('myKey', 'rb') as myKey:
            key = myKey.read()
        return key
    except FileNotFoundError:
        print("Key file 'myKey' not found. Please generate a key first.")

# Function for user file handling, allowing the user to input a file name and writing some lines to it
def user_file_handling():
    file_name = input('Name of the file to create: ')
    print(f'The file name is {file_name}')

    file_input = input('What do you want to be in the file: ')
    print(f'This will be file: {file_input}')

    try:
        with open(file_name, 'x') as file:  # 'x' mode creates a new file; raises an error if file exists
            file.write(file_input)
    except FileExistsError:
        print(f"File '{file_name}' already exists. Please choose a different file name.")

# Function for bigger premade file handling
def BIG_file_handling():
    if key is None:
        print("Fernet key not found. Please generate a key first.")
        return

    f = Fernet(key)

    name_of_file = input('What is the name of your file: ')
    encrypted_file_name = f'encrypted_{name_of_file}'  # Create a new file for the encrypted content

    try:
        with open(name_of_file, 'rb') as original_file:
            original = original_file.read()
            encrypted = f.encrypt(original)

        with open(encrypted_file_name, 'xb') as encrypted_file:  # 'xb' mode creates a new file; raises an error if file exists
            encrypted_file.write(encrypted)

        print(f'File {name_of_file} encrypted and saved as {encrypted_file_name}.')
    except FileNotFoundError:
        print(f"File '{name_of_file}' not found. Please provide a valid file name.")




def begining_input():
    file_option = input('Do you have a file(1) or are you making a file and putting input into it(2)')
    if file_option == '1':
        BIG_file_handling()
    elif file_option == '2':
        user_file_handling()



# Function to encrypt the contents of a file using a Fernet key and save it to a new file
def encrypting():
    f = Fernet(key)

    encrypt_file_input = input('What file do you want to encrypt: ')
    print(f'This file will be encrypted: {encrypt_file_input}')

    encrypt_file_output = input('What name do you want the new file to be? ')
    print(f'This is the new encrypted file name: {encrypt_file_output}')

    try:
        with open(encrypt_file_input, 'rb') as original_file:
            original = original_file.read()
            encrypted = f.encrypt(original)

        with open(encrypt_file_output, 'xb') as encrypted_file:  # 'xb' mode creates a new file; raises an error if file exists
            encrypted_file.write(encrypted)
    except FileNotFoundError:
        print(f"File '{encrypt_file_input}' not found. Please provide a valid file name.")
    except FileExistsError:
        print(f"File '{encrypt_file_output}' already exists. Please choose a different file name.")

# Uncomment the next line to generate and save a new Fernet key
generate_and_save_key()

# Read the Fernet key from the file
key = read_key_from_file()

#Gives user input to use premade file or make one
begining_input()

#Encrypt the contents of a file and save it to a new file
encrypting()
