#!/usr/bin/python3
# This program prints theASCII alphabet in reverse order
# While alternating lowercase and uppercase.
# Using one loop, no sotrage of characters in variable
# No importing any module

el = 0
for cha in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(cha - el)), end="")
    el = 32 if el == 0 else 0
