from termcolor import colored
def read_phone_numbers():
    print(colored("\t\t\t\tWELCOME TO THE PHONEBOOK PROGRAM!", 'magenta', attrs=["underline"]) )
    phonebook = {}
    while True:
        name = input(colored("Name: ", 'yellow'))
        if name == "":
            break
        number = input(colored("Number: ", 'yellow'))
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(colored(f"{name} -> {phonebook[name]}", 'cyan'))

def lookup_numbers(phonebook):
    while True:
        name = input(colored("Enter name to lookup: ", 'yellow'))
        if name == "":
            break
        if name not in phonebook:
            print(colored(f"{name} is not in the phonebook", 'red'))
        else:
            print(colored(phonebook[name], 'green'))
def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
