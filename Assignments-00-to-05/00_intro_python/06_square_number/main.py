from termcolor import colored
def square_number():
    print(colored("\t\t\t Welcome to the Square Number Program by Aleeza! ", "cyan", attrs=[ "underline"]))
    while True:
        try:
            number=int(input(colored("Enter a number: ", "light_magenta", attrs=["underline"]))
            )
            break
        except ValueError:              
            print(colored("❌ Invalid input! Please enter a valid number.", "red", attrs=[ "underline"]))
    square = number**2  
    print(colored(f"\nThe square of {number} is {square}.", "yellow", attrs=["underline"]))
    print(colored("\nThank you for using the Square Number Program! ", "cyan", attrs=[ "underline"]))
if __name__ == '__main__':
    square_number()