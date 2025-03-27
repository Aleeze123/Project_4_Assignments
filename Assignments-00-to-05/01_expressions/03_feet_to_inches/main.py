from termcolor import colored
def feet_to_inches():
    print(colored("\t\t\t Welcome to the Feet to Inches Program by Aleeza! ", "yellow", attrs=[ "underline"]))
    while True:
        try:
            feet=int(input(colored("Enter the number of feet: ", "light_magenta", attrs=["underline"]))
            )
            break
        except ValueError:              
            print(colored("❌ Invalid input! Please enter a valid number.", "red", attrs=[ "underline"]))
    inches = feet*12  
    print(colored(f"\n{feet} feet is equal to {inches} inches.", "cyan", attrs=["underline"]))
    print(colored("\nThank you for using the Feet to Inches Program! ", "yellow", attrs=[ "underline"]))
if __name__ == '__main__':
    feet_to_inches()

