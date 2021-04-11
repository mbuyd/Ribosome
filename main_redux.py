'''
Redux version of main.py

For variables in ALL_CAPS, these are constants. You can hover your mouse
over them in VS code to see the constant they hold.
'''

import re
import json


# CONSTANTS for use in the rest of the script
DATA_FILE = 'databank_redux.json'
RNA_INPUT_PROMPT = 'Enter your RNA sequence: '
ALLOWED_RNA_CHARACTERS = ['A', 'C', 'G', 'U']
ERROR_THYMINE_IN_SEQUENCE = 'Thymine cannot be present in the RNA sequence, make sure that you are using the RNA sequence.'
ERROR_NUMBER_IN_SEQUENCE = 'Integers should not be in the sequence. Make sure to remove 5\' and 3\' if they are present.'
# Number of RNA characters to check at a time
CHECK_SIZE = 3


# Compiled constants
ALLOWED_RNA_CHARACTER_STRING = ''.join(ALLOWED_RNA_CHARACTERS)
ERROR_EXTRANEOUS_CHARACTERS = f'RNA can only have the following characters in its set: {ALLOWED_RNA_CHARACTER_STRING}'


# Regular expression for use in the rest of the script
HAS_NUMBER = re.compile('[0-9]+')
HAS_EXTRANEOUS_CHARACTERS = re.compile(f'[^{ALLOWED_RNA_CHARACTER_STRING}]+')


def transform_data(data: dict) -> dict:
    '''
    Takes your databank and transforms it to a more efficient format. This
    format is harder to read, but is easier and faster for the computer
    to process. It also assumes that everything in your databank is unique,
    and will work as long as the databank is unique.
    '''
    better_data = dict()
    for key in data:
        # data[key] is your array and item is each item in the array
        for item in data[key]:
            better_data[item.upper()] = key.upper()
    return better_data


def verify_valid_rna(sequence: str, force_fail=False) -> bool:
    '''
    Checks if the input sequence is a valid RNA string... I guess?

    By default, it'll return True or False. Setting force_fail=True will cause
    the function to only return True, and end the program otherwise.
    '''
    # All checks to perform
    has_no_thymine = 'T' not in sequence
    has_no_numbers = not HAS_NUMBER.search(sequence)
    has_no_extraneous = not HAS_EXTRANEOUS_CHARACTERS.search(sequence)

    # Runs if we want the program to exit on failure
    if force_fail:
        assert has_no_thymine, ERROR_THYMINE_IN_SEQUENCE
        assert has_no_numbers, ERROR_NUMBER_IN_SEQUENCE
        assert has_no_extraneous, ERROR_EXTRANEOUS_CHARACTERS
        return True
    
    # Runs if we don't want the program to exit on failure, and return False instead
    else:
        return has_no_thymine and has_no_numbers and has_no_extraneous


def translate(sequence: str, data: dict) -> str:
    '''
    Returns a translated sequence... I guess?

    Give it an input sequence and the better_data as data.
    '''
    result_sequence = str()

    # Remove groups of three characters from our sequence and add it to
    # the new one until there are no more to check
    while len(sequence) > 0:
        # Next three characters to check
        check = sequence[:CHECK_SIZE]

        # If we can translate it from our data table, translate it
        if check in data:
            result_sequence += data[check]
        # Otherwise... print the original sequence?
        else:
            result_sequence += check

        # Remove the first three characters
        sequence = sequence[CHECK_SIZE:]
    
    return result_sequence


# This runs when the file is called from the terminal
if __name__ == '__main__':
    data = json.load(open(DATA_FILE))
    # .upper() transforms the string to all uppercase
    sequence = input(RNA_INPUT_PROMPT).upper()
    better_data = transform_data(data)
    translated_sequence = translate(sequence, better_data)
    print(f'Your result translation was: {translated_sequence}')
