from termcolor import colored
def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_cost = 0
    print(colored("\t\t\t\tWelcome to the Fruit Shop!", 'magenta', attrs=['underline']))
    for fruit_name in fruits:
        price = fruits[fruit_name]
        while True:
            try:
                amount_bought = input(colored(f"How many ({fruit_name}) do you want to buy?: ", 'yellow'))
                if amount_bought == "":  
                    amount_bought = 0
                    break
                amount_bought = int(amount_bought)
                break  
            except ValueError:
                print(colored("Invalid input! Please enter a valid number.", 'red'))
        total_cost += (price * amount_bought)
    
    print(colored(f"\nYour total is Rs{total_cost:.2f}", 'green'))
if __name__ == '__main__':
    main()
