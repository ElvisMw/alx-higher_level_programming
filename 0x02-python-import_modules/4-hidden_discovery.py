#!/usr/bin/python3
# This program prints all the names defined by the
# compiled module hidden_4.pyc names that do not start with __
if __name__ == "__main__":
    import hidden_4
    for name in sorted(dir(hidden_4)):
        if name[:2] != '__':
            print("{}".format(name))
