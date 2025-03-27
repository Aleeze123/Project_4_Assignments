from termcolor import colored
import math
def pythagorean_theorem():
    print(colored("\t\t\t WELCOME TO THE PYTHAGOREAN THEOREM PROGRAM BY ALEEZA! ", "yellow", attrs=["underline"]))
    while True:
        try:
            ab = float(input(colored("Enter the length of side AB: ", "light_magenta", attrs=["underline"])))
            ac = float(input(colored("Enter the length of side AC: ", "light_magenta", attrs=["underline"])))
            bc = math.sqrt(ab**2 + ac**2)
            print(colored(f"The length of BC (the hypotenuse) is: {bc}", "cyan", attrs=["bold"]))
            print(colored("\nThank you for using the Pythagorean Theorem Program!", "yellow", attrs=["underline"]))
        except ValueError:
            print(colored("❌ Invalid input! Please enter valid numbers for the sides.", "red", attrs=["underline"]))
if __name__ == '__main__':
    pythagorean_theorem()
