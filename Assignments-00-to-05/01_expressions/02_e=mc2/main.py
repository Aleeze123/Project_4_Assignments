from termcolor import colored
def main():
    print(colored("\t\t\t Welcome to the E=mc^2 Program by Aleeza⚡", "cyan", attrs=["underline"]))
    c = 299792458  
    while True:
        try:
            mass_in_kg = float(input(colored("Enter kilos of mass:", "white", attrs=["underline"])))
            break 
        except ValueError:
            print(colored("❌ Please enter a valid number! ❌", "red"))
    energy_in_joules = mass_in_kg * (c ** 2)
    print(colored("e = m * C^2... ⚡", "magenta"))
    print(colored(f"m = {mass_in_kg} kg ", "cyan"))
    print(colored(f"C = {c} m/s 🚀", "magenta"))
    print(colored(f"{energy_in_joules} joules of energy! ⚡💥", "yellow"))
    print(colored("Thank you for using the E=mc^2 Program...", "green"))
if __name__ == '__main__':
    main()

