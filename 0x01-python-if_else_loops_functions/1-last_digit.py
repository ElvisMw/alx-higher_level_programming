#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
less_than_six = "and is less than 6 and not 0"
if number < 0:
    last_digit = -last_digit
    print(f"Last digit of {number} is {last_digit} {less_than_six}")
else:
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    elif last_digit < 6 and last_digit != 0:
        print(f"Last digit of {number} is {last_digit} {less_than_six}")
