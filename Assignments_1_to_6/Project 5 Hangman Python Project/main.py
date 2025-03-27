import random
import string
from termcolor import colored

def choose_word():
    word_list = ["python", "java", "javascript", "ruby", "swift", "go", "html", "css"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)

def hangman():
    print(colored("Welcome to Hangman!", "cyan", attrs=["bold"]))
    
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        print(colored(f"\nRemaining Attempts: {attempts}", "yellow"))
        print(colored(f"Word: {display_word(word, guessed_letters)}", "green"))
        
        guess = input(colored("\nGuess a letter: ", "magenta")).lower()
        
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print(colored("Invalid input. Please guess a single letter.", "red"))
            continue
        
        if guess in guessed_letters:
            print(colored("You already guessed that letter. Try again.", "red"))
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(colored(f"Good guess! '{guess}' is in the word.", "blue"))
        else:
            attempts -= 1
            print(colored(f"Oops! '{guess}' is not in the word.", "red"))
        
        if all(letter in guessed_letters for letter in word):
            print(colored(f"\nCongratulations! You guessed the word: {word}", "green"))
            break
    else:
        print(colored(f"\nGame Over! The word was: {word}", "red"))
if __name__ == "__main__":
    hangman()
