from termcolor import colored
def tiny_mad_lib():
    print(colored("\t\t\t Welcome to the Tiny Mad Lib Program by Aleeza! 📝", "yellow", attrs=["underline"]))
    adjective: str = input(colored("Enter an adjective: ", "magenta"))
    noun: str = input(colored("Enter a noun: ", "magenta"))
    verb: str = input(colored("Enter a verb: ", "magenta"))
    print(colored(f"\nPanaversity is fun. I learned to program and used Python to {verb} a {adjective} {noun}.", "cyan", attrs=["bold"]))
    print(colored("\nThank you for using the Tiny Mad Lib Program by Aleeza!", "yellow", attrs=["underline"]))
if __name__ == '__main__':
    tiny_mad_lib()