from termcolor import colored
def print_events():
    for i in range(20):
        print(colored(i * 2, 'cyan')) 
if __name__ == "__main__":
    print_events()
