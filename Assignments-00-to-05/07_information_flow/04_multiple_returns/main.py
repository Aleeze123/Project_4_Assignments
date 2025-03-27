from termcolor import colored
def get_user_info():
    first_name = input(colored("What is your first name?: ", "cyan"))
    last_name = input(colored("What is your last name?: ", "cyan"))
    email_address = input(colored("What is your email address?: ", "cyan"))
    return first_name, last_name, email_address
def main():
    user_data = get_user_info()
    print(colored(f"Received the following user data: {user_data}", "yellow"))

if __name__ == "__main__":
    main()
