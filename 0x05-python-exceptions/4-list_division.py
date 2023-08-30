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
    new_list = []
    for e in range(0, list_length):
        try:
            division_result = my_list_1[e] / my_list_2[e]
        except TypeError:
            print("wrong type")
            division_result = 0
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        finally:
            new_list.append(division_result)
    return new_list
