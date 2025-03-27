from termcolor import colored
def count_even(lst):
    """
    Returns the number of even numbers in the list and prints the result.
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = 0  
    for num in lst:  
        if num % 2 == 0: 
            count += 1 
    print(colored(f"Number of even numbers: {count}", "cyan")) 
def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    Handles invalid inputs gracefully.
    """
    lst = []  
    while True:
        user_input = input(colored("Enter an integer or press enter to stop: ", "yellow"))  
        if user_input == "": 
            break
        try:
            lst.append(int(user_input)) 
        except ValueError:
            print(colored("That's not a valid integer! Please try again.", "red"))  
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst) 

if __name__ == '__main__':
    main()
