#!/usr/bin/python3
""" The function in study prints the input text with 2 new lines after
each of the characters: ., ? and"""


def text_indentation(text):
    """Print text with 2 new lines when '.', '?', and ':' are encountered

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    e_m = 0
    while e_m < len(text) and text[e_m] == ' ':
        e_m += 1

    while e_m < len(text):
        print(text[e_m], end="")
        if text[e_m] == "\n" or text[e_m] in ".?:":
            if text[e_m] in ".?:":
                print("\n")
            e_m += 1
            while e_m < len(text) and text[e_m] == ' ':
                e_m += 1
            continue
        e_m += 1
