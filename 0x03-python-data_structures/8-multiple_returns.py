#!/usr/bin/python3
""" This function returns a tuple with the
length of a string & its 1st character.
Not allowed to import any module"""


def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]

    return length, first
