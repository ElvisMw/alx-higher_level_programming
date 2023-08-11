#!/usr/bin/python3
# This a program that imports functions
# from the file calculator_1.py, does some Maths,
# and prints the result

from calculator_1 import add, sub, mul, div

a = 10
b = 5

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
