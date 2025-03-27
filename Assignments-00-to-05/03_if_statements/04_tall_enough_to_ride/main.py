from termcolor import colored

MINIMUM_HEIGHT = 50

def main():
    print(colored("\t\t\t\tWelcome to the Tall Enough to Ride Checker!", 'cyan'))
    height = float(input(colored("How tall are you? ", 'yellow')))
    
    if height >= MINIMUM_HEIGHT:
        print(colored("You're tall enough to ride!", 'green'))
    else:
        print(colored("You're not tall enough to ride, but maybe next year!", 'red'))

if __name__ == '__main__':
    main()
