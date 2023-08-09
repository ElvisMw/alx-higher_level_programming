#!/usr/bin/python3


def print_last_digit(number):
    number_1 = abs(number) % 10
    print(f"{number_1}", end="")
    return(number_1)
