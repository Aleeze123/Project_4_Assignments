import random
from termcolor import colored
print(colored("\t\t\t Welcome to the Dice Simulator Program by Aleeza🎲 ", "yellow", attrs=["underline"]))
NUM_SIDES = 6
def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(colored(f"Rolled: {die1} and {die2} - Total: {total}", "cyan", attrs=["bold"]))
def main():
    die1 = 10
    print(colored(f"die1 in main() starts as: {die1}", "magenta"))
    roll_dice()
    roll_dice()
    roll_dice()
    print(colored(f"die1 in main() is still: {die1}", "magenta"))
if __name__ == '__main__':
    main()
