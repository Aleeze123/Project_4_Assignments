from termcolor import colored 
def get_name():
    return "Aleeza"  
def main():
    name = get_name() 
    print(colored(f"Howdy {name} 😍", "cyan"))  
if __name__ == '__main__':
    main()
