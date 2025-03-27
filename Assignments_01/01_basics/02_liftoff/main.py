from termcolor import colored

def main():
    for i in range(10, 0, -1):
        print(colored(i, 'yellow'), end=" ")

    print(colored("Liftoff!", 'magenta'))

if __name__ == '__main__':
    main()
