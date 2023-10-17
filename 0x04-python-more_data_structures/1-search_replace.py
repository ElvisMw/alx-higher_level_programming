#!/usr/bin/python3
# This function that replaces all occurrences of
# an element by another in a new list.
# Prototype is: def search_replace(my_list, search, replace):
# 'my_list' is the initial list.
# 'Search' is the element to replace in the list.
# 'replace' is the new element.
# Not allowed to import any module

def search_replace(my_list, search, replace):
    nu_list = list(map(lambda x: replace if x == search else x, my_list))
    return nu_list
