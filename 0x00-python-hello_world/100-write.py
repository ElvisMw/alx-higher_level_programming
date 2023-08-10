#!/usr/bin/python3
# Python script that prints exactly "and that
# piece of art is useful - Dora Korpar, 2015-10-19",
# followed by a new line, using the function write
# from the sys module
# Not allowed to use print
# The script should print to stderr
# The script should exit with the status code 1

import sys

sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)

