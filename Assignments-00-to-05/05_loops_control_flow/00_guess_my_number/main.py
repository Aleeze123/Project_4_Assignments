import random
from termcolor import colored
def main():
    secret_number = random.randint(1, 99)
    print(colored("\t\t\t\t Welcome to the number guessing game!", 'magenta', attrs=["underline"]))
    print(colored("I am thinking of a number between 1 and 99...", 'yellow'))
    while True:
        try:
            guess = int(input(colored("Enter a guess: ", 'cyan')))
            break
        except ValueError:
            print(colored("Invalid input! Please enter a valid number.", 'red'))
    while guess != secret_number:
        if guess < secret_number:
            print(colored("Your guess is too low.", 'blue'))
        else:
            print(colored("Your guess is too high.", 'blue'))    
        print() 
        while True:
            try:
                guess = int(input(colored("Enter a new guess: ", 'cyan')))  
                break
            except ValueError:
                print(colored("Invalid input! Please enter a valid number.", 'red'))   
    print(colored(f"Congrats! The number was: {secret_number}", 'green'))
if __name__ == '__main__':
    main()
