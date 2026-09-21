# --------------------------------------------------
# Joshua Herrick
# CSD-205325
# Module 2.2 Assignment
#
# Purpose:
# Using this previous assignment to demonstrate debugging
# --------------------------------------------------

# --------------------------------------------------
# Recursive Function
# --------------------------------------------------

def recursive_count(n):
    print(f"\n--- Starting recursive_count({n}) ---")

    if n == 1:
        print(1)
    else:
        recursive_count(n - 1)
        print(n)

    print(f"--- Ending recursive_count({n}) ---")

# --------------------------------------------------
# Non-Recursive Function
# --------------------------------------------------

def non_recursive_count(n):
    print(f"\n--- Starting non_recursive_count({n}) ---")

    for number in range(1, n + 1):
        print(number)

    print(f"--- Ending non_recursive_count({n}) ---")

# --------------------------------------------------
# Main Program

# --------------------------------------------------

while True:
    try:
        n = int(input("\nEnter a positive integer: "))

        if n > 0:
            break

        print("Invalid entry. Please enter a number greater than 0.")

    except ValueError:
        print("Invalid entry. Please enter a whole number.")


# --------------------------------------------------
# Run Recursive Function
# --------------------------------------------------

recursive_count(n)


# --------------------------------------------------
# Run Non-Recursive Function
# --------------------------------------------------

non_recursive_count(n)

# --------------------------------------------------
# Keep Console Window Open
# --------------------------------------------------

input("\nPress Enter to exit...")