#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics"""


def print_stats(size, status_codes):
    """
    Reads stdin line by line and computes metrics based on
    the provided input format.

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C), prints
    those statistics since the beginning.

    Parameters:
    - size (int): The total file size calculated based on the
    input lines.
    - status_codes (dict): A dictionary containing the counts of
    each status code encountered in the input lines.

    Note:
    - The script reads input from stdin and computes statistics based
    on the provided format.
    - It calculates and prints the total file size and
    the number of lines for each valid status code.
    - Status codes are printed in ascending order.

    Example:
    >>> cat 101-generator.py | ./101-stats.py
    File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
    File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3
    File size: 16305
    200: 3
    301: 3
    400: 4
    401: 2
    403: 5
    404: 5
    405: 4
    500: 4
    ...
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
