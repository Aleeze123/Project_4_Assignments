from termcolor import colored
def Add_numbers():
    print(colored("\t\t\t Welcome to the Number Adder Program by Aleeza! ", "yellow", attrs=["bold", "underline", "reverse"]))
    def get_number(prompt, color):
        while True:
            try:
                return int(input(colored(f"\n{prompt}", color, attrs=["bold", "underline"])))
            except ValueError:
                print(colored("❌ Invalid input! Please enter a valid number. ❌", "red", attrs=["bold", "underline"]))
    num1 = get_number("🔢 Enter the first number: ", "magenta")
    num2 = get_number("🔢 Enter the second number: ", "blue")
    total = num1 + num2
    print(colored(f"\n The total sum is: {total} ", "cyan", attrs=["bold", "underline", "reverse"]))
    print(colored("\nThank you for using the program!", "green", attrs=["bold"]))
if __name__ == '__main__':
    Add_numbers()
