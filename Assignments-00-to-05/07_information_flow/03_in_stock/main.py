from termcolor import colored
def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        return 0
def main():
    fruit = input(colored("Enter a fruit: ", "yellow"))
    stock = num_in_stock(fruit)
    if stock == 0:
        print(colored("This fruit is not in stock.", "red"))
    else:
        print(colored("This fruit is in stock! Here is how many:", "green"))
        print(colored(stock, "blue"))
if __name__ == '__main__':
    main()
