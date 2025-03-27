from termcolor import colored 
def double(num: int):
    """
    This function takes an integer and returns its double.
    """
    return num * 2
def main():
    while True:
        try:
            num = int(input(colored("Enter a number: ", "cyan")))
            num_times_2 = double(num)
            print(colored(f"Double that is {num_times_2}", "magenta"))
            break  
        except ValueError:
            print(colored("That's not a valid number! Please enter a valid integer.", "red"))
if __name__ == '__main__':
    main()
