import random
from termcolor import colored
def play_game():
    choices = ["rock", "paper", "scissors"]
    print(colored("Welcome to Rock, Paper, Scissors! 🪨📄✂️", "cyan", attrs=["bold"]))
    
    user_choice = input(colored("Enter 'rock', 'paper', or 'scissors': ", "yellow")).lower()
    
    if user_choice not in choices:
        print(colored("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.", "red"))
        return
    computer_choice = random.choice(choices)
    print(f"\n{colored('Computer\'s choice:', 'green')} {colored(computer_choice, 'magenta')}")
    
    if user_choice == computer_choice:
        print(colored("It's a tie! 🤝", "blue"))
    elif user_choice == "rock" and computer_choice == "scissors":
        print(colored("You win! Rock beats Scissors. 🪨 > ✂️", "green"))
    elif user_choice == "paper" and computer_choice == "rock":
        print(colored("You win! Paper beats Rock. 📄 > 🪨", "green"))
    elif user_choice == "scissors" and computer_choice == "paper":
        print(colored("You win! Scissors beats Paper. ✂️ > 📄", "green"))
    else:
        print(colored("You lose! Better luck next time. 😔", "red"))

if __name__ == "__main__":
    play_game()
