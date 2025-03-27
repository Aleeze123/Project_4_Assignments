from termcolor import colored
def temperature():
    print(colored("\t\t\t Welcome to the Fahrenheit to Celsius Converter Program by Aleeza! ", "white", attrs=["bold", "underline", "reverse"]))
    while True:
        try:
            fahrenheit = float(input(colored("Enter the temperature in Fahrenheit:", "light_magenta", attrs=["bold"])))
            celsius = (fahrenheit - 32) * 5.0 / 9.0
            print(colored(f"\n{fahrenheit}°F is equal to {celsius}°C. 🌡️", "cyan", attrs=["bold", "underline"]))
            break
        except ValueError:
            print(colored("Oops! That doesn't seem like a valid temperature. Please enter a number! ", "red", attrs=["bold"]))
    print(colored("\nThank you for using the Fahrenheit to Celsius Converter Program!", "yellow", attrs=["bold", "underline"]))
if __name__ == '__main__':
    temperature()
