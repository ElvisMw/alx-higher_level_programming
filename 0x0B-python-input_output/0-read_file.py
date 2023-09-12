#!/usr/bin/python3
"""This function reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Read the contents of a text file and print them to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")

if __name__ == "__main__":
    read_file("my_file_0.txt")
