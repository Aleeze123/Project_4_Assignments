from termcolor import colored

def main():
    print(colored("\t\t\t\tWelcome to the Leap Year Checker!", 'cyan'))
    year = int(input(colored('Please input a year: ', 'yellow')))
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(colored("That's a leap year!", 'green'))
            else:
                print(colored("That's not a leap year.", 'red'))
        else:
            print(colored("That's a leap year!", 'green'))
    else:
        print(colored("That's not a leap year.", 'red'))
    

if __name__ == '__main__':
    main()
