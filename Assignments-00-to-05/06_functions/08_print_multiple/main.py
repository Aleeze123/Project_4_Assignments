from termcolor import colored

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(colored(message, 'magenta'))

def main():
    message = input(colored("Please type a message: ", "yellow"))
    repeats = int(input(colored("Enter a number of times to repeat your message: ", "yellow")))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
