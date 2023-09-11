#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

print(my_list)
"""
Creates a MyList object and appends integers to it. Prints the original list.

Example:
    Output:
    [1, 4, 2, 3, 5]
"""

my_list.print_sorted()
"""
Sorts and prints the MyList object in ascending order.

Example:
    Output:
    [1, 2, 3, 4, 5]
"""

print(my_list)
"""
Prints the MyList object after sorting, which remains unchanged.

Example:
    Output:
    [1, 2, 3, 4, 5]
"""
