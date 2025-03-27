from termcolor import colored
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes."
def main():
    user_input = input(colored(PROMPT, "yellow")).strip().lower()
    if user_input == "joke":
        print(colored(JOKE, "cyan"))
    else:
        print(colored(SORRY, "red"))
if __name__ == "__main__":
    print(colored("Welcome to the Joke Bot program by Aleeza! 🤖", "magenta"))
    main()