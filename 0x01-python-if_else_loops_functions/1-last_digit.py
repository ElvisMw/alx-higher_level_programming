#!/usr/bin/python3
# This codes prints the last digit and a random number
# and states if its greater than 5
# or its 0
# or its less than 6 and not 0

import random
number = random.randint(-10000, 10000)
last_digit = (number % 10)
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
