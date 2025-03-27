from termcolor import colored
print(colored("\t\t\t Welcome to the Triangle Perimeter Calculator Program by Aleeza! ", "yellow", attrs=["underline"]))
def get_side(prompt, color):
    while True:
        try:
            side = float(input(colored(prompt, color)))
            return side
        except ValueError:
            print(colored("❌ Invalid input! Please enter a valid number.❌", "red", attrs=["underline"]))
def calculate_perimeter():
    side1 = get_side("What is the length of side 1? ", "magenta")
    side2 = get_side("What is the length of side 2? ", "magenta")
    side3 = get_side("What is the length of side 3? ", "magenta")
    perimeter = side1 + side2 + side3
    print(colored(f"\nThe perimeter of the triangle is {perimeter} units.", "cyan", attrs=["underline"]))
    print(colored("\nThank you for using the Triangle Perimeter Calculator Program! ", "yellow", attrs=["underline"]))
if __name__ == '__main__':
    calculate_perimeter()
