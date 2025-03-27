import random
from termcolor import colored

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100
def main():
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    colored_numbers = [colored(str(num), 'cyan') for num in random_numbers]
    print(" ".join(colored_numbers))
if __name__ == '__main__':
    main()
