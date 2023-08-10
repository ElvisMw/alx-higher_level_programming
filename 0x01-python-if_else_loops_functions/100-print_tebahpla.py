#!/usr/bin/python3

for i in range(25, -1, -1):
    print(chr(ord('a') + i).upper()
            if i % 2 == 0
            else chr(ord('a') + i), end="")

