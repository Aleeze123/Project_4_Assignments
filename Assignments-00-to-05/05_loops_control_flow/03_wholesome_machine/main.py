from termcolor import colored

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print(colored("Please type the following affirmation: ", 'magenta') + colored(AFFIRMATION, 'yellow'))
    
    user_feedback = input()  
    while user_feedback != AFFIRMATION:  
        print(colored("Hmmm", 'red'))
        print(colored("That was not the affirmation.", 'red'))
        
        print(colored("Please type the following affirmation: ", 'magenta') + colored(AFFIRMATION, 'yellow'))
        user_feedback = input()

    print(colored("That's right! 😊", 'green'))

if __name__ == '__main__':
    main()
