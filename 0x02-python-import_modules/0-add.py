#!/usr/bin/python3

"""
This program imports the function def add(a, b):
from the file add_0.py & prints the result
of the addition 1 + 2 = 3
It uses print function with string format to display integers
The code signs assign:
1. the value 1 to a variable called a
2. the value 2 to a variable called b
- The two variables are used as arguments when
calling the functions add and print
- a and b must be defined in 2 different lines: a = 1 and another b = 2
- The program prints: <a value> + <b value> = <add(a, b) value>
followed with a new line
- Only use the word add_0 once in your code
- Not allowed to use * for importing or __import__
Your code should not be executed when imported - by using __import__
"""

if __name__ == '__main__':
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
