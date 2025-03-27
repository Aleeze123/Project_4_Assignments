from termcolor import colored
def main():
    print(colored("\t\t\t\t First 20 Even Numbers", 'magenta', attrs=["underline"]))
    print(colored("The first 20 even numbers are:", 'yellow', attrs=["underline"]))
    for i in range(20):
        print(colored(i * 2, 'cyan'))  
if __name__ == "__main__":
    main()
