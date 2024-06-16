from multiprocessing.sharedctypes import Value
import random
import string
from xml.etree.ElementInclude import include

passwords = []

def get_password_criteria(): # Asks user for length and include_symbols criteria
    while True:
        try:
            print()
            length = int(input("Desired password length (minimum 8): "))
            if length < 8:
                print("Password length should be at least 8.")
                continue
        except ValueError:
            print("Please print a valid number.")
            continue

        while True:
            include_symbols_input = input("Include symbols? (yes/no): ").strip().lower()
            if include_symbols_input =='yes':
                include_symbols = True
                return length, include_symbols
            elif include_symbols_input == 'no':
                include_symbols = False
                return length, include_symbols
            else:
                print("Please enter 'yes' or 'no'.")

def generate_password(length, include_symbols): # Generates password based on user criteria
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_password(password): # Saves password to passwords list
    while True:
        usage = input("What will this password be used for?: ").strip()
        if usage:
            passwords.append({"usage": usage, "password": password})
            print("Password saved!")
            break
        else:
            print("Usage description cannot be empty.")

def view_passwords(): # Allows user to view passwords saved to passwords list
    if len(passwords) == 0:
        print()
        print("No saved passwords.")
    else:
        index = 1
        print()
        for entry in passwords:
            print(f"{index}. Usage: {entry['usage']}, Password: {entry['password']}")
            index += 1

def main():
    while True:
        print("\nMenu:")
        print("1. Generate a new password")
        print("2. View saved passwords")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            length, include_symbols = get_password_criteria()
            password = generate_password(length, include_symbols)
            print(f"Generated password: {password}")
            save = input("Would you like to save this password? (yes/no): ").lower()
            while save not in ['yes', 'no']:
                print("Please enter 'yes' or 'no'.")
                save = input("Would you like to save this password? (yes/no): ").lower()
            if save == 'yes':
                save_password(password)
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            print("Exiting the program.")
            print()
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

