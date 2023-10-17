#!/usr/bin/python3
"""This function that inserts a line of text to a file, after...
each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a
    specific string.

    This function reads the content of the specified file, and
    for each line that contains
    the 'search_string', it appends the 'new_string' to
    the end of that line.
    It then writesthe modified content back to the file.

    Parameters:
    - filename (str): The name of the file to operate on.
    - search_string (str): The string to search for in each
    line of the file.
    - new_string (str): The string to insert after each
    line containing the 'search_string'.

    Note:
    - This function uses the 'with' statement to safely handle file
    operations.
    - It does not manage file permission or file does not exist exceptions.

    Example:
    >>> append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
    >>> # Contents of append_after_100.txt after execution:
    >>> # At School,
    >>> # Python is really important,
    >>> # "C is fun!"
    >>> # "C is fun!"
    >>> # But it can be very hard if:
    >>> # - You don't get all Pythonic tricks
    >>> # "C is fun!"
    >>> # "C is fun!"
    >>> # - You don't have strong C knowledge.
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)
