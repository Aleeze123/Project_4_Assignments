from termcolor import colored
def main():
    print(colored("\t\t\t\tWelcome to the Doubling Program!", 'magenta', attrs=["underline"]))
    curr_value = int(input(colored("Please enter a number: ", 'cyan')))
    while curr_value < 100:
        curr_value *= 2
        print(colored(curr_value, 'yellow'))

if __name__ == '__main__':
    main()
