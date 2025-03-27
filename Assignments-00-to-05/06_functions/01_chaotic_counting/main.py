from termcolor import colored
import random

DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(colored(curr_num, 'green'))

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print(colored("I'm going to count until 10 or until I feel like stopping, whichever comes first.", 'yellow'))
    chaotic_counting()
    print(colored("I'm done", 'blue'))

if __name__ == "__main__":
    main()
