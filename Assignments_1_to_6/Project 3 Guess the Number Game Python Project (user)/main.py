import random
from termcolor import colored
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    print(colored("\t\t\t\t WELOCME TO GUESS THE NUMBER GAME", "cyan" , attrs=["underline"]))
    print(colored("I'm thinking of a number between 1 and 100. Can you guess it?", "yellow"))
    attempts = 0
    while True:
        guess = input(colored("\nEnter your guess: ", "green"))
        if not guess.isdigit():
            print(colored("❌ Please enter a valid number!", "red"))
            continue
        guess = int(guess)
        attempts += 1
        if guess < number_to_guess:
            print(colored("Too low! Try again.", "blue"))
        elif guess > number_to_guess:
            print(colored("Too high! Try again.", "magenta"))
        else:
            print(colored(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts. ", "green"))
            break
if __name__ == "__main__":
    guess_the_number()
