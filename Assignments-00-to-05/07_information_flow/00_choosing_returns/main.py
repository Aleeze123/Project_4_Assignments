from termcolor import colored

ADULT_AGE = 18

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    while True:
        try:
            age = int(input(colored("How old is this person?: ", "yellow")))
            print(colored(is_adult(age), "cyan"))
            break
        except ValueError:
            print(colored("That's not a valid number! Please enter a valid integer.", "red"))

if __name__ == "__main__":
    main()
