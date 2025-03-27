from termcolor import colored

name = input(colored("Enter a name: ", "cyan"))
place = input(colored("Enter a place: ", "magenta"))
animal = input(colored("Enter an animal: ", "yellow"))
adjective = input(colored("Enter an adjective: ", "green"))
verb = input(colored("Enter a verb: ", "blue"))
story = f"One day, {name} went to {place} and saw a {adjective} {animal}. It {verb} and everyone was amazed!"
print(colored("\nHere's your Mad Libs story:", "red", attrs=["bold"]))
print(colored(story, "white", attrs=["underline"]))
print(colored("Thank you for playing!", "magenta"))
