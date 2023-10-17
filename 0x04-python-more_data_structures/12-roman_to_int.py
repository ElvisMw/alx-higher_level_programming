#!/usr/bin/python3
# This function def roman_to_int(roman_string):converts
# a Roman numeral to an integer.
# Assumption: The number will be between 1 to 3999.
# def roman_to_int(roman_string) must return an integer
# If the roman_string is not a string or None, return 0


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_dict[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value

    return total
