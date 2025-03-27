from termcolor import colored
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60
def seconds_in_year():
    print(colored("\t\t\t Welcome to the Seconds in a Year Program by Aleeza! ⏳", "yellow", attrs=["underline"]))
    total_seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    print(colored(f"There are {total_seconds_in_year} seconds in a year!", "green", attrs=["bold"]))
if __name__ == '__main__':
    seconds_in_year()
