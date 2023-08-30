#!/ussr/bin/python3
# This function executes a function safely.
# The prototype is: def safe_function(fct, *args):
# assumption: fct will be always a pointer to a function
# Returns the result of the function,
# Otherwise, returns None if something happens during
# the function and prints in stderr the error precede by Exception:
# try: / except: is used.


import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
