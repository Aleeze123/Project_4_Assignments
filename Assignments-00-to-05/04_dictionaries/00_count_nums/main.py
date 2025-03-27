from termcolor import colored
def get_user_numbers():
    print(colored("\t\t\t\tWELCOME TO THE NUMBER COUNTER PROGRAM!", 'magenta', attrs=["underline"]) )
    user_numbers = []
    while True:
        user_input = input(colored("Enter a number: ", 'yellow'))
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers
def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict
def print_counts(num_dict):
    for num in num_dict:
        print(colored(f"{num} appears {num_dict[num]} times.", 'cyan'))
def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)
if __name__ == '__main__':
    main()
