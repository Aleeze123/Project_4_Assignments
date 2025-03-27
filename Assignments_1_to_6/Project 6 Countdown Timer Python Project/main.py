import time
from termcolor import colored

def countdown_timer(seconds):
    print(colored(f"Countdown starting from {seconds} seconds...", "cyan", attrs=["bold"]))
    while seconds > 0:
        minutes, secs = divmod(seconds, 60) 
        time_format = f"{minutes:02d}:{secs:02d}"
        print(colored(f"\r{time_format}", "green"), end="")
        time.sleep(1) 
        seconds -= 1

    print(colored("\nTime's up! ⏰", "red"))

if __name__ == "__main__":
    try:
        user_input = int(input(colored("Enter time in seconds for countdown: ", "yellow")))
        countdown_timer(user_input)
    except ValueError:
        print(colored("Invalid input. Please enter a valid number of seconds.", "red"))
