"""
Brian Horner
CS 521 - Summer 1
Date: 6/15/2021
Homework Problem: 5_6_3
This program takes three int values from the user and divides the first int by
the second and adds that to the third. It returns the value.
"""


def number_calculations(first_int, second_int, third_int):
    """This function takes three int values and divides the first int by the
    second and adds that to the third. It returns the value."""
    while True:
        try:
            # Converting inputs to floats
            first_int, second_int, third_int = float(first_int), \
                                               float(second_int), \
                                               float(third_int)
            # Dividing first number by second number and adding to third number
            third_int += first_int/second_int
            return third_int
        # Error catch for items that can not be converted to floats or not
        # three inputs
        except ValueError:
            print(f"Error invalid input. Your input can not be converted for "
                  f"calculations. Please check input and try again.")
            break
        # Error catch for dividing by zero
        except ZeroDivisionError:
            print(f"Error your first number: {first_int} is not divisible by "
                  f"your second int: {second_int}")
            break


if __name__ == '__main__':
    # Gathering user input
    first_number, second_number, third_number = input("Enter three numbers with "
                                                      "spaces in between: ").split()
    # Print output that shows the formula applied and result of calculation
    print(f"Your number after the formula {third_number} + ({first_number} /"
          f" {second_number}) is:"
          f"  {number_calculations(first_number, second_number, third_number)}")
else:
    print("Error: This module is not meant to be imported. Please consult "
          "developer.")
