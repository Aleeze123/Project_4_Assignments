from termcolor import colored
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48
def main():
    print(colored("Welcome to the International Voting Age Checker!", "cyan"))
    user_age = int(input(colored("How old are you? ", "yellow")))
    if user_age >= PETURKSBOUIPO_AGE:
        print(colored(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.", "green"))
    else:
        print(colored(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.", "red"))
    
    if user_age >= STANLAU_AGE:
        print(colored(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.", "green"))
    else:
        print(colored(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.", "red"))
    
    if user_age >= MAYENGUA_AGE:
        print(colored(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.", "green"))
    else:
        print(colored(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.", "red"))
if __name__ == '__main__':
    main()
