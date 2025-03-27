import random
from termcolor import colored

def computer_guess():
    print(colored("Think of a number between 1 and 100 and I will try to guess it!", "cyan", attrs=["bold"]))
    input(colored("Press Enter when you are ready.", "yellow"))
    
    low = 1
    high = 100
    attempts = 0
    
    while True:
        guess = random.randint(low, high)
        attempts += 1
        
        print(colored(f"My guess is: {guess}", "green"))
        user_feedback = input(colored("Is my guess too high, too low, or correct? (Enter 'high', 'low', or 'correct'): ", "magenta")).lower()
        
        if user_feedback == "correct":
            print(colored(f"I guessed your number {guess} in {attempts} attempts!", "blue", attrs=["bold"]))
            break
        elif user_feedback == "high":
            high = guess - 1
        elif user_feedback == "low":
            low = guess + 1
        else:
            print(colored("Invalid input. Please enter 'high', 'low', or 'correct'.", "red"))

if __name__ == "__main__":
    computer_guess()
