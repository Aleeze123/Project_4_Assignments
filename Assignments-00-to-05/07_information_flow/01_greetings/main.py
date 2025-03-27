from termcolor import colored

def greet(name):
    return "Greetings " + name + "!"

def main():
    name = input(colored("What's your name? ", "yellow"))
    print(colored(greet(name), "cyan"))

if __name__ == '__main__':
    main()
