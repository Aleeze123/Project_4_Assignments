from termcolor import colored
import random
NUM_SIDES: int = 6
def roll_dice():
    print(colored("\t\t\t Welcome to the Dice Rolling Program by Aleeza! 🎲", "yellow", attrs=["underline"]))
    input(colored("Press Enter to roll the dice... ", "green"))
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(colored(f"\nRolling the dice...\n", "magenta", attrs=["bold"]))
    print(colored(f"First die: {die1}", "cyan", attrs=["bold"]))
    print(colored(f"Second die: {die2}", "magenta", attrs=["bold"]))
    print(colored(f"\nTotal of two dice: {total}", "green", attrs=["bold"]))
    print(colored("\nThank you for using the Dice Rolling Program by Aleeza!", "blue", attrs=["underline"]))
def main():
    roll_dice()
if __name__ == '__main__':
    main()
