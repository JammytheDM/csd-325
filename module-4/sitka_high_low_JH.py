import csv
from datetime import datetime

from matplotlib import pyplot as plt

# --------------------------------------------------
# Joshua Herrick
# CSD-325 Module 4.2
# Sitka High and Low Temperature Program
#
# Changes made:
# 1. Added instructions for using the menu.
# 2. Added a menu for Highs, Lows, and Exit.
# 3. Added low temperature data collection.
# 4. Added a blue graph for low temperatures.
# 5. Added a loop so the menu continues until Exit
#    is selected.
# 6. Added an exit message.
# --------------------------------------------------

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures.
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)


# --------------------------------------------------
# Menu instructions
# --------------------------------------------------

print("\nSitka Weather Temperature Viewer")
print("--------------------------------")
print("Enter 'Highs' to view the daily high temperatures.")
print("Enter 'Lows' to view the daily low temperatures.")
print("Enter 'Exit' to quit the program.")


# --------------------------------------------------
# Main menu loop
# --------------------------------------------------

while True:
    choice = input("\nChoose Highs, Lows, or Exit: ").strip().lower()

    # --------------------------------------------------
    # High temperatures
    # --------------------------------------------------

    if choice == 'highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # --------------------------------------------------
    # Low temperatures
    # --------------------------------------------------

    elif choice == 'lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    # --------------------------------------------------
    # Exit
    # --------------------------------------------------

    elif choice == 'exit':
        print("\nThank you for using the Sitka Weather Temperature Viewer!")
        print("Goodbye!")
        break

    # --------------------------------------------------
    # Invalid menu choice
    # --------------------------------------------------

    else:
        print("\nInvalid choice.")
        print("Please enter Highs, Lows, or Exit.")