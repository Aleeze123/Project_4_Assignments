from termcolor import colored

def liftoff():
    print(colored("\t\t\t\t Liftoff Countdown", 'magenta', attrs=["underline"]))
    for i in range(10, 0, -1):
        print(colored(i, 'cyan'))
    print(colored("Liftoff!", 'green'))

if __name__ == '__main__':
    liftoff()
