"""
Brian Horner
CS 521 - Summer 1
Date: 6/15/2021
Homework Problem: 5_15_5
This program calculates the compound interest of an account with a standard
function and a recursive function and returns the inputs.
"""


def calc_compound_interest(principal, int_rate, years):
    """Function calculates the ending value of an account with the principal
    amount, interest rate, and years."""
    return principal * ((1+int_rate) ** years)

# Could not figure out how to fix this to work ran out of time.
def calc_recursive(principal, int_rate, years):
    """Could not figure out how to do this recusively. It kept saying I
    needed positional arguments 'int_rate' and 'years' I assume because of
    the *"""
    if years == 0:
        return principal
    else:
#         # compound_interest_recursive(principal*(1+rate), rate, years-1
        return calc_recursive(principal*((1 + int_rate) ** (years-1)))
    pass

if __name__ == '__main__':

    # True loop that breaks if valid input or user types in 'Quit'
    while True:
        principal_value = input("Enter the principal value: ")
        interest_rate = input("Enter the interest rate as a decimal: ")
        years = input("Enter the years: ")
        try:
            principal_value = float(principal_value)
            interest_rate = float(interest_rate)
            years = float(years)
            print(f"You entered the Principal Value of: "
                  f"{principal_value} Interest Rate of: "
                  f"{interest_rate} and {int(years)} years.")
            print(f" Your compound interest is "
                  f"{calc_compound_interest(principal_value, interest_rate, years):,.2f}")
            # print(f" Your compound interest is calculated recursively is "
            #       f"{calc_recursive(principal_value, interest_rate, years):,.2f}")
            break
        except ValueError:
            print("Error: Your input is not valid.")
            principal_value = int(input("Enter the principal value: "))
            interest_rate = int(input("Enter the interest rate as a decimal: "))
            years = int(input("Enter the years:"))
            print("Enter 'Quit' in order to exit the program.")


else:
    print("Error: Module not formatted for importing yet. Please see "
          "developer.")


# Print if the two values are equal when rounded to 4 decimal places

# Ran out of time and couldn't do this or recursive function. Sorry work was
# to busy this week.
