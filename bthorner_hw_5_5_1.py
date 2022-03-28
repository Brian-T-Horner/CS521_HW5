"""
Brian Horner
CS 521 - Summer 1
Date: 6/15/2021
Homework Problem: 5_5_1
This program takes an English sentence from the user and returns the number
of vowels and consonants in sentence.
"""


def vc_counter(input_str):
    """This function takes an string and counts the consonants and vowels.
    It adds the totals to a to dictionary for returning """
    # Vowels constant
    VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']
    # Establishing dictionary for vowels and consonants counts
    vowels_consontants_count_dict = {'total_vowels': 0, 'total_consonants': 0}
    character_count_list = [char.upper() for char in input_str.strip() if
                            char.isalpha()]
    # Iterating over character count list and checking if not a vowel
    for char in character_count_list:
        # If not vowel adding a count to dictionary key
        if char not in VOWELS:
            vowels_consontants_count_dict['total_consonants'] += 1
        else:
            # Adding a count to vowels key
            vowels_consontants_count_dict['total_vowels'] += 1
    # Returning dictionary with counts for vowels and consonants
    return vowels_consontants_count_dict


def pretty_print_v2(input_str):
    """This function takes the inputs of the vc_counter function and
    prints clean statements."""
    print(f"Sentence entered into program: {input_str} ")
    # Calling vc_counter function in print statements with get function for
    # each key
    print(f"Total # of vowels in sentence: "
          f"{(vc_counter(input_str)).get('total_vowels')}")
    print(f"Total # of consonants in sentence: "
          f"{(vc_counter(input_str).get('total_consonants'))} ")


if __name__ == '__main__':

    # Taking sentence input from user
    user_sentence_input = input("Enter an English sentence in order to count "
                                "the consonants and vowels.")
    # Calling pretty print on user_sentence_input
    pretty_print_v2(user_sentence_input)


else:
    print("Error: Why did you import this? Consult the developer for "
          "clarification.")
