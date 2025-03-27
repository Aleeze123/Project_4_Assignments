from termcolor import colored
def remainder_division():
    print(colored("\t\t\t WELCOME TO THE REMAINDER DIVISION PROGRAM BY ALEEZA", "yellow", attrs=["underline"]))
    while True:
        try:
            dividend: int = int(input(colored("Please enter an integer to be divided: ", "light_magenta", attrs=["underline"])))
            divisor: int = int(input(colored("Please enter an integer to divide by: ", "light_magenta", attrs=["underline"])))
            quotient = dividend // divisor
            remainder = dividend % divisor  
            print(colored(f"The result of this division is {quotient} with a remainder of {remainder}.", "cyan", attrs=["reverse", "bold"]))
            break  
        except ValueError:  
            print(colored("❌ Invalid input! Please enter a valid number.", "red", attrs=["underline"]))
        except ZeroDivisionError:  
            print(colored("❌ You cannot divide by zero! Please enter a valid number.", "red", attrs=["underline"]))
    print(colored("\nThank you for using the Remainder Division Program!", "yellow", attrs=["underline"]))
if __name__ == '__main__':
    remainder_division()
