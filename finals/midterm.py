import os
import math

# ENABLE COLORS IN WINDOWS CMD
os.system("")

# COLOR MODULE
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"


# DESIGN MODULE
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def line():
    print(CYAN + "+" + "-" * 53 + "+" + RESET)


def header(title):
    line()
    print(CYAN + BOLD + "|" + title.center(53) + "|" + RESET)
    line()


def pause():
    input(YELLOW + "\n  Press ENTER to continue..." + RESET)


# MODULE 1: VALID INTEGER INPUT
def get_integer(message):
    while True:
        try:
            value = int(input(YELLOW + "  " + message + RESET))

            if value <= 0:
                print(RED + "  [!] Enter a number greater than zero." + RESET)
            else:
                return value

        except ValueError:
            print(RED + "  [!] Invalid input! Enter a whole number." + RESET)


# MODULE 2: VALID FLOAT INPUT
def get_float(message):
    while True:
        try:
            value = float(input(YELLOW + "  " + message + RESET))

            if not math.isfinite(value) or value < 0:
                print(RED + "  [!] Enter a valid non-negative amount." + RESET)
            else:
                return value

        except ValueError:
            print(RED + "  [!] Invalid amount! Try again." + RESET)


# MODULE 3: GET TRAVEL INFORMATION
def get_travel_info():

    clear_screen()
    header("TRAVEL INFORMATION")

    destination = input(YELLOW + "\n  Destination: " + RESET)

    while not destination.strip():
        print(RED + "  [!] Destination cannot be empty." + RESET)
        destination = input(YELLOW + "  Destination: " + RESET)

    print(CYAN + "\n  TRAVEL DETAILS" + RESET)

    travelers = get_integer("Number of travelers: ")
    nights = get_integer("Number of nights: ")

    print(PURPLE + "\n  EXPENSE INFORMATION" + RESET)

    transportation = get_float("Transportation per traveler: P")
    accommodation = get_float("Accommodation per night: P")
    food = get_float("Food allowance per day: P")
    miscellaneous = get_float("Miscellaneous expenses: P")
    budget = get_float("Available budget: P")

    return [
        destination, travelers, nights,
        transportation, accommodation,
        food, miscellaneous, budget
    ]


# MODULE 4: CALCULATE BUDGET
def calculate_budget(info):

    transportation = info[1] * info[3]
    accommodation = info[2] * info[4]
    food = info[1] * info[2] * info[5]
    miscellaneous = info[6]

    expenses = [
        transportation,
        accommodation,
        food,
        miscellaneous
    ]

    total = sum(expenses)
    per_traveler = total / info[1]

    return expenses, total, per_traveler


# MODULE 5: DISPLAY RESULTS
def display_result(info, expenses, total, per_traveler):

    clear_screen()
    header("TRAVEL BUDGET REPORT")

    print(CYAN + BOLD + "\n  TRAVEL INFORMATION" + RESET)
    print(WHITE + f"  Destination       : {info[0]}" + RESET)
    print(WHITE + f"  Travelers         : {info[1]}" + RESET)
    print(WHITE + f"  Number of Nights  : {info[2]}" + RESET)

    line()

    print(PURPLE + BOLD + "\n  COST BREAKDOWN" + RESET)

    labels = [
        "Transportation",
        "Accommodation",
        "Food / Daily Expenses",
        "Miscellaneous"
    ]

    for i in range(len(expenses)):
        print(
            WHITE + f"  {labels[i]:<27}" +
            GREEN + f"P {expenses[i]:>14,.2f}" + RESET
        )

    line()

    print(CYAN + BOLD + "\n  TRIP SUMMARY" + RESET)

    print(WHITE + f"  Total Trip Cost       : " +
          GREEN + f"P {total:,.2f}" + RESET)

    print(WHITE + f"  Cost Per Traveler     : " +
          GREEN + f"P {per_traveler:,.2f}" + RESET)

    line()

    print(PURPLE + BOLD + "\n  BUDGET STATUS" + RESET)

    budget = info[7]

    print(WHITE + f"  Available Budget     : P {budget:,.2f}" + RESET)

    if total < budget:
        remaining = budget - total

        print(GREEN + f"  Remaining Budget     : P {remaining:,.2f}" + RESET)
        print(GREEN + BOLD + "\n  STATUS: WITHIN BUDGET" + RESET)

    elif total == budget:
        print(GREEN + "  Remaining Budget     : P 0.00" + RESET)
        print(GREEN + BOLD + "\n  STATUS: EXACTLY ON BUDGET" + RESET)

    else:
        deficit = total - budget

        print(RED + f"  Budget Deficit       : P {deficit:,.2f}" + RESET)
        print(RED + BOLD + "\n  STATUS: OVER BUDGET" + RESET)

    line()

    print(CYAN + BOLD +
          "\n       THANK YOU FOR USING OUR SYSTEM!" + RESET)

    line()


# MAIN PROGRAM
while True:

    clear_screen()

    print(CYAN + BOLD)
    print("  +-----------------------------------------------------+")
    print("  |                                                     |")
    print("  |              TRAVEL BUDGET ESTIMATOR                |")
    print("  |                                                     |")
    print("  |          PLAN YOUR TRIP. MANAGE YOUR MONEY.         |")
    print("  |                                                     |")
    print("  +-----------------------------------------------------+")
    print(RESET)

    print(PURPLE + BOLD + "\n  MAIN MENU" + RESET)
    line()

    print(GREEN + "    [1] " + WHITE + "Estimate Travel Budget" + RESET)
    print(RED + "    [2] " + WHITE + "Exit Application" + RESET)

    line()

    try:
        choice = int(input(YELLOW + "\n  Select an option: " + RESET))

        if choice == 1:

            info = get_travel_info()

            expenses, total, per_traveler = calculate_budget(info)

            display_result(
                info, expenses, total, per_traveler
            )

            pause()

        elif choice == 2:

            clear_screen()
            header("APPLICATION EXIT")

            print(GREEN + BOLD +
                  "\n       Thank you for using our system!" + RESET)

            print(CYAN + "             Have a safe trip!" + RESET)

            line()
            break

        else:
            print(RED + "\n  [!] Invalid choice! Select 1 or 2." + RESET)
            pause()

    except ValueError:
        print(RED + "\n  [!] Please enter a valid menu number." + RESET)
        pause()
