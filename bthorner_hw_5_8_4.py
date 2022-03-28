"""
Brian Horner
CS 521 - Summer 1
Date: 6/15/2021
Homework Problem: 5_8_4
This program takes a file with text and returns the unique words found.
"""
import string


def list_to_once_words(input_file):
    """This function takes an input file of text and returns a list
    containing unique words used once."""
    list_of_words = []
    # Iterating through file lines
    for lines in input_file:
        # splitting lines into words and taking out punctuation
        for word in lines.strip().split():
            word = ''.join([char for char in word if char not in
                                    string.punctuation and char.isdigit() ==
                            False])
            # Appending words to list of words if they are not digits
            list_of_words.append(word.lower())
            # Adding unique words to a unique word list
            unique_word_list = [word for word in list_of_words if
                                    list_of_words.count(word) <= 1]

    return unique_word_list


def pretty_print_v2(returned_list):
    """"This function cleans the list into a string for printing. You can
    take this function out and the calling of this function for just a list.
    I did not like how it looked outputted."""
    unique_word_str = ", ".join(returned_list)
    return unique_word_str


if __name__ == '__main__':

    while True:
        try:
            # Opening file in with statement to avoid closing errors
            with open("bthorner_hw_5_8_4_input.txt", "r") as input_file:
                # Printing output of functions
                print(f"The unique words in your file are:"
                      f" {pretty_print_v2(list_to_once_words(input_file))}")

            break
        # Handling error if file is not found
        except FileNotFoundError:
            print("Error: Your input file is not found. Please correct and "
                  "try again.")
            break
else:
    print("What are you doing? Why did you do this? Don't import this. Please "
          "consult developer.")

