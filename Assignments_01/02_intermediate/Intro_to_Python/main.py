from termcolor import colored
def main():
    try:
        earth_weight = float(input(colored("Enter a weight on Earth: ", "yellow")))
        planet = input(colored("Enter a planet: ", "yellow"))
        planet_gravity = {
            "Mercury": 0.376,
            "Venus": 0.889,
            "Mars": 0.378,
            "Jupiter": 2.36,
            "Saturn": 1.081,
            "Uranus": 0.815,
            "Neptune": 1.14
        }
        if planet in planet_gravity:
            gravity = planet_gravity[planet]
            planetary_weight = earth_weight * gravity
            print(colored(f"The equivalent weight on {planet}: {round(planetary_weight, 2)}", "green"))
        else:
            print(colored("Invalid planet name. Please enter a valid planet name from the solar system.", "red"))
    except ValueError:
        print(colored("Invalid input for weight. Please enter a valid number.", "red"))
if __name__ == '__main__':
    main()
