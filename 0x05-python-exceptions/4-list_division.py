#!/usr/bin/python3
# This function divides element by element 2 lists.
# Prototype is:def list_division(my_list_1, my_list_2, list_length):
# my_list_1 and my_list_2 can contain any type (integer, string, etc.)
# list_length can be bigger than the length of both lists
# Returns a new list (length = list_length) with all divisions
# If 2 elements can’t be divided, the division result should
# be equal to 0
# If an element is not an integer or float:
# -print: wrong type
# If the division can’t be done (/0):
# -print: division by 0
# If my_list_1 or my_list_2 is too short
# -print: out of range
# try: / except: / finally: is used
# not allowed to import any module

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for e in range(list_length):
        try:
            value_1 = my_list_1[e] if e < len(my_list_1) else 0
            value_2 = my_list_2[e] if e < len(my_list_2) else 0

            if not isinstance(value_1, (int, float)) or not isinstance(value_2, (int, float)):
                print("wrong type")
                result.append(0)
            elif value_2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(value_1 / value_2)
        except IndexError:
            print("out of range")
            result.append(0)

    return result
