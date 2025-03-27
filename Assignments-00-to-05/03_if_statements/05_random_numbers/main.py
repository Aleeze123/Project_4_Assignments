import random
from termcolor import colored

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print(colored("\t\t\t\tWelcome to the random number generator!", 'magenta', attrs=["underline"]))
    for _ in range(N_NUMBERS):
        print(colored(random.randint(MIN_VALUE, MAX_VALUE), 'cyan'))

if __name__ == '__main__':
    main()
