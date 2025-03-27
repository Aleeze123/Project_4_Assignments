import random
import string
from termcolor import colored
def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    character_pool = string.ascii_lowercase 
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    password = ''.join(random.choice(character_pool) for i in range(length))
    return password
def main():
    print(colored("Welcome to the Password Generator! 🔐", "cyan", attrs=["bold"]))
    
    try:
        length = int(input(colored("Enter the desired password length: ", "yellow")))
        if length < 6:
            print(colored("Password length must be at least 6 characters.", "red"))
            return
        use_uppercase = input(colored("Include uppercase letters? (yes/no): ", "magenta")).lower() == 'yes'
        use_numbers = input(colored("Include numbers? (yes/no): ", "magenta")).lower() == 'yes'
        use_special_chars = input(colored("Include special characters? (yes/no): ", "magenta")).lower() == 'yes'
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        
        print(colored("\nHere is your generated password:", "green"))
        print(colored(password, "yellow", attrs=["bold"]))
    
    except ValueError:
        print(colored("Invalid input. Please enter a valid number for the password length.", "red"))

if __name__ == "__main__":
    main()
