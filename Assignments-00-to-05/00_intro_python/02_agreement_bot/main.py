from termcolor import colored
def favorite_animal():
    print(colored("\t\t\t Welcome to the Agreement Bot Program by Aleeza! ", "yellow", attrs=["bold", "underline", "reverse"]))
    while True:
        try:
            favorite_animal = input(colored("What's your favorite animal? ", "light_cyan", attrs=["bold"]))
            if not favorite_animal.isalpha():
                raise ValueError("Oops! That doesn't seem like a valid animal. Please enter a word that represents an animal!")
            break 
        except ValueError as e:
            print(colored(str(e), "red", attrs=["bold"]))
    print(colored(f"\nMy favorite animal is also {favorite_animal}!", "magenta", attrs=["bold", "underline"]))
    print(colored("\nThank you for using the Agreement Bot Program! ", "green", attrs=["bold", "underline"]))
if __name__ == '__main__':
    favorite_animal()
