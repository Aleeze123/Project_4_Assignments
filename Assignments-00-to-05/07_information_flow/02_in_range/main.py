from termcolor import colored

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    try:
        n = int(input(colored("Enter the number (n): ", "yellow")))
        low = int(input(colored("Enter the low range: ", "yellow")))
        high = int(input(colored("Enter the high range: ", "yellow")))

        if in_range(n, low, high):
            print(colored(f"{n} is between {low} and {high}.", "green"))
        else:
            print(colored(f"{n} is not between {low} and {high}.", "red"))
    
    except ValueError:
        print(colored("Please enter valid integers for all inputs.", "red"))

if __name__ == '__main__':
    main()
