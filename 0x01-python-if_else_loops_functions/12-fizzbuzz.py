#!/usr/bin/python3
# This is a function that prints the
# numbers from 1 to 100 separated by a space.
# For multiples of 3 print Fizz instead of the
# number and for multiples of 5 print Buzz
# For numbers which are multiples of both
# 3 and 5 print FizzBuzz.
# Each element should be followed by a space

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(f"{number}", end=" ")
