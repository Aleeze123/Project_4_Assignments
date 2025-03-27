import random
from termcolor import colored

NUM_ROUNDS = 5
score = 0

def main():
    global score
    try:
        print(colored("Welcome to the High-Low Game!", 'blue'))
        print(colored("--------------------------------", 'blue'))

        for round_num in range(1, NUM_ROUNDS + 1):
            print(f"\n{colored(f'Round {round_num}', 'yellow')}")

            your_number = random.randint(1, 100)
            computer_number = random.randint(1, 100)

            print(f"{colored('Your number is', 'green')} {your_number}")

            user_guess = input(colored("Do you think your number is higher or lower than the computer's?: ", 'cyan')).strip().lower()

            while user_guess not in ["higher", "lower"]:
                user_guess = input(colored("Please enter either 'higher' or 'lower': ", 'red')).strip().lower()

            if user_guess == "higher":
                if your_number > computer_number:
                    print(f"{colored('You were right! The computer\'s number was', 'green')} {computer_number}")
                    score += 1
                else:
                    print(f"{colored('Aww, that\'s incorrect. The computer\'s number was', 'red')} {computer_number}")
            elif user_guess == "lower":
                if your_number < computer_number:
                    print(f"{colored('You were right! The computer\'s number was', 'green')} {computer_number}")
                    score += 1
                else:
                    print(f"{colored('Aww, that\'s incorrect. The computer\'s number was', 'red')} {computer_number}")

            print(f"{colored('Your score is now', 'blue')} {score}")

        print(colored("\nThanks for playing!", 'magenta'))
        print(f"{colored('Your final score is:', 'magenta')} {score}")

        if score == NUM_ROUNDS:
            print(colored("Wow! You played perfectly!", 'yellow'))
        elif score >= NUM_ROUNDS // 2:
            print(colored("Good job, you played really well!", 'yellow'))
        else:
            print(colored("Better luck next time!", 'red'))

    except Exception as e:
        print(colored(f"An error occurred: {e}", 'red'))

if __name__ == '__main__':
    main()
