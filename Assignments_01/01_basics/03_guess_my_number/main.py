import random
from termcolor import colored

def main():
    try:
        secret_number: int = random.randint(1, 99)
        print(colored("I am thinking of a number between 1 and 99...", "yellow"))
        
        guess = int(input(colored("Enter a guess: ", "yellow")))
        
        while guess != secret_number:
            if guess < secret_number:
                print(colored("Your guess is too low", "red"))
            else:
                print(colored("Your guess is too high", "blue"))
                
            print()
            guess = int(input(colored("Enter a new guess: ", "yellow")))
            
        print(colored("Congrats! The number was: " + str(secret_number), "green"))
    
    except ValueError:
        print(colored("Please enter a valid integer as your guess.", "red"))

if __name__ == '__main__':
    main()
