from termcolor import colored
def print_ones_digit(num):
    ones_digit = num % 10
    print(colored(f"The ones digit is {ones_digit}", "cyan"))
def main():
    while True:
        try:
            num = int(input(colored("Enter a number: ", "yellow")))
            print_ones_digit(num)
            break  
        except ValueError:
            print(colored("That's not a valid number! Please enter a valid integer.", "red"))
if __name__ == '__main__':
    main()
