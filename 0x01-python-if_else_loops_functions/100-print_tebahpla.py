#!/usr/bin/python3

el = 0
for cha in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(cha - el)), end="")
    el = 32 if el == 0 else 0


