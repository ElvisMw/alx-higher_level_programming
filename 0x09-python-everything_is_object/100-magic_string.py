#!/usr/bin/python3
def magic_string():
    magic_string.e = getattr(magic_string, 'e', 0) + 1
    return ("BestSchool, " * (magic_string.e - 1) + "BestSchool")
