import os
from random import choice, random
import json
import re

# CONSTANTS for use in the rest of the script
DATA_FILE = 'Databank.json'
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
    better_data = dict()
    for key in data:
        # data[key] is your array and item is each item in the array
        for item in data[key]:
            better_data[item.upper()] = key.upper()
    return better_data

def translate(sequence: str, data: dict) -> str:
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
    has_thymine = 'T' in sequence
    has_numbers = HAS_NUMBER.search(sequence)
    has_extraneous = HAS_EXTRANEOUS_CHARACTERS.search(sequence)
    if has_thymine:
        print(ERROR_THYMINE_IN_SEQUENCE) 
        force_fail=True
    elif has_numbers:
        print(ERROR_NUMBER_IN_SEQUENCE) 
        force_fail=True
    elif has_extraneous:
        print (ERROR_EXTRANEOUS_CHARACTERS) 
        force_fail=True
    else:
        translated_sequence = translate(sequence, better_data)
        print(f'Your result translation was: {translated_sequence}')