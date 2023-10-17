#!/usr/bin/python3
# This is function that prints last digit of number
# and returns the value of the last digit

def print_last_digit(number):
    number_1 = abs(number) % 10
    print(f"{number_1}", end="")
    return (number_1)
