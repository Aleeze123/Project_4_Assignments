from hashlib import sha256
from termcolor import colored
print(colored("\t\t\t\t\t\t  WELCOME TO THE POWERFUL PASSWORD PROGRAM!", 'yellow', attrs=["underline"]))
def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    if stored_logins.get(email) == hash_password(password_to_check):
        return True
    return False
def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """
    return sha256(password.encode()).hexdigest()
def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }

    result = login("example@gmail.com", stored_logins, "word")
    print(colored(f"Login attempt for example@gmail.com with password 'word': {result}", 'red' if not result else 'cyan'))
    
    result = login("example@gmail.com", stored_logins, "password")
    print(colored(f"Login attempt for example@gmail.com with password 'password': {result}", 'cyan' if result else 'red'))
    
    result = login("code_in_placer@cip.org", stored_logins, "Karel")
    print(colored(f"Login attempt for code_in_placer@cip.org with password 'Karel': {result}", 'red' if not result else 'cyan'))
    
    result = login("code_in_placer@cip.org", stored_logins, "karel")
    print(colored(f"Login attempt for code_in_placer@cip.org with password 'karel': {result}", 'red' if not result else 'cyan'))
    
    result = login("student@stanford.edu", stored_logins, "password")
    print(colored(f"Login attempt for student@stanford.edu with password 'password': {result}", 'red' if not result else 'cyan'))
    
    result = login("student@stanford.edu", stored_logins, "123!456?789")
    print(colored(f"Login attempt for student@stanford.edu with password '123!456?789': {result}", 'red' if not result else 'cyan'))

if __name__ == '__main__':
    main()
