"""
Brian Horner
CS 521 - Summer 1
Date: 6/15/2021
Homework Problem: 5_5_2
This program takes a user inputted time and date as (MM/DD/YY HH:mm:SS) and
checks if the input is valid. If it is valid it returns it in various
formats. If it is not it delivers curated error messages. This module may not be
the most efficient way. I cut out a lot of internal function comments as the
doc strings and error messages seemed to clarify what was going on.
"""


def is_leap_year(year):
    """Determines if year is a leap year or not."""
    year = int(year)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year):
    """Determines the days in February based on is_leap_year function
    returning True or False."""
    if is_leap_year(year):
        valid_days_in_month = [31, 29, 31, 30,
                               31, 30, 31, 31,
                               30, 31, 30, 31
                               ]
        return valid_days_in_month
    elif not is_leap_year(year):
        valid_days_in_month = [31, 28, 31, 30,
                               31, 30, 31, 31,
                               30, 31, 30, 31
                               ]
        return valid_days_in_month


def valid_month(month):
    """Checks if user inputted month is valid."""
    valid_months = ['01', '02', '03', '04',
                    '05', '06', '07', '08',
                    '09', '10', '11', '12']
    if month in valid_months:
        return True
    else:
        print("Error: Your month either does not have the required amount "
              "of digits or is formatted incorrectly. Try formatting your "
              "month as MM.")


def valid_year(year):
    """Checks if user inputted year is valid"""
    if year.isnumeric and len(year) == 4:
        return True
    else:
        print("Error: Your year either does not have the required amount "
              "of digits or is formatted incorrectly. Try formatting your "
              "year as YYYY.")


def valid_day(month, day, year):
    """Checks if user inputted day is valid. Uses days_in_month to make sure
    user inputted day is not greater than allow days in month."""
    valid_days = ['01', '02', '03', '04', '05', '06',
                  '07', '08', '09', '10', '11', '12',
                  '13', '14', '15', '16', '17', '18',
                  '19', '20', '21', '22', '23', '24',
                  '25', '26', '27', '28', '29', '30',
                  '31'
                  ]
    # Calling days in month to determine
    days_in_month(year)
    month_index_value = (int(month)) - 1
    if day in valid_days and int(day) <= int(days_in_month(year)[
                                                               month_index_value]):
        return True
    else:
        print("Error: Your day either does not have the required amount "
              "of digits or is formatted incorrectly. Try formatting your "
              "day as DD. (Be sure to check for leap years).")


def valid_minutes(minutes):
    """Checks if user inputted minutes are valid."""
    valid_mins = ['00', '01', '02', '03', '04', '05',
                  '06', '07', '08', '09', '10', '11',
                  '12', '13', '14', '15', '16', '17',
                  '18', '19', '20', '21', '22', '23',
                  '24', '25', '26', '27', '28', '29',
                  '30', '31', '32', '33', '34', '35',
                  '36', '37', '38', '39', '40', '41',
                  '42', '43', '44', '45', '46', '47',
                  '48', '49', '50', '51', '52', '53',
                  '54', '55', '56', '57', '58', '59',
                  ]
    if minutes in valid_mins:
        return True
    else:
        print("Error: Your minute input is invalid. It is either formatted "
              "incorrectly or does not fall within the acceptable minutes in "
              "an hour. Try formatting your minutes as mm.")


def valid_hour(hour):
    """Checks if user inputted hour is valid."""
    valid_hours = ['00', '01', '02', '03', '04', '05',
                   '06', '07', '08', '09', '10', '11',
                   '12', '13', '14', '15', '16', '17',
                   '18', '19', '20', '21', '22', '23',
                   ]
    if hour in valid_hours:
        return True
    else:
        print("Error: Your hour is either formatted incorrectly or does "
              "not fall between the standard 24 hours in an Earth day. "
              "Try formatting your hour as HH.")


def valid_second(secs):
    """Checks if user inputted seconds are valid."""

    valid_seconds = ['00', '01', '02', '03', '04', '05',
                     '06', '07', '08', '09', '10', '11',
                     '12', '13', '14', '15', '16', '17',
                     '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29',
                     '30', '31', '32', '33', '34', '35',
                     '36', '37', '38', '39', '40', '41',
                     '42', '43', '44', '45', '46', '47',
                     '48', '49', '50', '51', '52', '53',
                     '54', '55', '56', '57', '58', '59',
                     ]
    if secs in valid_seconds:
        return True
    else:
        print("Error: Your seconds are either formatted incorrectly or do not "
              "fall between the standard 24 hours in an Earth day. "
              "Try formatting your seconds as ss.")


def am_or_pm(input_str):
    """Checks to see if user inputted time is in the AM or PM."""
    # Splitting up the inputs into specified variables
    user_date, user_time = input_str.split(" ")
    user_hour, user_minutes, user_seconds = user_time.split(":")

    # Establishing am_hours and pm_hours
    am_hours = ['00', '01', '02', '03',
                '04', '05', '06', '07',
                '08', '09', '10', '11',
                ]
    pm_hours = ['12', '13', '14', '15',
                '16', '17', '18', '19',
                '20', '21', '22', '23',
                ]
    # If hour in am return AM else if in pm return PM
    if user_hour in am_hours:
        return "AM"
    elif user_hour in pm_hours:
        return "PM"
    # This should not run unless something seriously breaks
    else:
        print("Error this should not occur since the validity of the input "
              "was checked before")


def day_month_year(input_str):
    """Formats user inputted date and time into DD/MM/YYYY."""
    # Splitting input up into date and month variables
    user_date, user_time = input_str.split(" ")
    # Splitting date variable up
    user_month, user_day, user_year = user_date.split("/")
    day_month_year_list = [user_day, user_month, user_year]
    # Returning list with .join to correct formatting
    return "/".join(day_month_year_list)
    pass


def hour_min_sec(input_str):
    """Formats user inputted date and time into HH/mm/SS."""
    # Splitting input up into date and month variables
    user_date, user_time = input_str.split(" ")
    user_hour, user_minutes, user_seconds = user_time.split(":")
    hour_min_sec_list = [user_hour, user_minutes, user_seconds]
    # Returning list with .join to correct formatting
    return ":".join(hour_min_sec_list)


def month_year(input_str):
    """Formats user inputted date and time in MM/YYYY."""
    user_date, user_time = input_str.split(" ")
    user_month, user_day, user_year = user_date.split("/")
    month_year_list = [user_month, user_year]
    return "/".join(month_year_list)


def is_valid_datetime(input_str):
    """Checks if user inputted string is a valid date and time. If so returns
    True else returns False"""
    try:
        user_date, user_time = input_str.split(" ")
        user_month, user_day, user_year = user_date.split("/")
        user_hour, user_minutes, user_seconds = user_time.split(":")
        if valid_month(user_month):
            if valid_day(user_month, user_day, user_year):
                if valid_year(user_year):
                    if valid_hour(user_hour):
                        if valid_minutes(user_minutes):
                            if valid_second(user_seconds):
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except ValueError:
        # This pass allows a user to quit without seeing the error message below
        if input_str == "Quit":
            pass
        else:
            print("Error: Your input is formatted incorrectly or contains "
                  "characters that are not accepted. Your input should be in "
                  "the following format, (MM/DD/YYYY HH:mm:SS")


if __name__ == '__main__':

    # Taking user input
    user_input = input("Enter a date and time with the format (MM/DD/YYYY "
                       "HH:mm:SS): ")
    # True loop that breaks if valid input or user types in 'Quit'
    while True:
        if is_valid_datetime(user_input):
            print(f"You entered {user_input}.")
            print(f"Your inputted date formatted as DD/MM/YYY"
                  f"Y: {day_month_year(user_input)}")
            print(f"Your inputted time formatted as HR:MIN:SEC: "
                  f"{hour_min_sec(user_input)}")
            print(f"Your inputted date formatted as MM/YYYY:"
                  f" {month_year(user_input)}")
            print(f"Your inputted time is in the {am_or_pm(user_input)}")
            break
        elif user_input == "Quit":
            break
        else:
            # Prints quit in case user wants to quit.
            print("Enter 'Quit' in order to exit the program.")
            user_input = input("Enter a date and time with the format (MM/DD/YY "
                               "HH:mm:SS): ")

else:
    print("Error: Module not formatted for importing yet. Please see "
          "developer.")
