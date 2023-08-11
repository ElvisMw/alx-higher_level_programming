#!/usr/bin/python3
"""
This program imports the function def add(a, b):
from the file add_0.py and prints the result
of the addition 1 + 2 = 3
It uses print function with string format to display integers
You have to assign:
the value 1 to a variable called a
the value 2 to a variable called b
The two variables are used as arguments when
calling the functions add and print
- a and b must be defined in 2 different lines: a = 1 and another b = 2
- The program prints: <a value> + <b value> = <add(a, b) value>
followed with a new line
- Only use the word add_0 once in your code
- Not allowed to use * for importing or __import__
Your code should not be executed when imported - by using __import__
"""
from add_0 import add
if __name__ == '__main__':
    a = 1
    b = 2
    result = a + b
    print(f"{a} + {b} = {result}")
