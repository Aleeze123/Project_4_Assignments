from termcolor import colored

def average(a: float, b: float):
    sum = a + b
    return sum / 2
def main():
    
    print(colored("\t\t\t\tCalculating average", "magenta", attrs=["underline"]))
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    final = average(avg_1, avg_2)
    print(colored(f"avg_1: {avg_1}", "green"))
    print(colored(f"avg_2: {avg_2}", "cyan"))
    print(colored(f"final: {final}", "yellow"))
if __name__ == '__main__':
    main()
