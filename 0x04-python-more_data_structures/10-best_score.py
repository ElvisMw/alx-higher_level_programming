#!/usr/bin/python3
# Now this function returns a key with the biggest integer value
# Assumption_1: All values are only integers.
# Assumption_2: All students have a different score.
# Return 'None' if no score found.
# Forbidden to import any module.


def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
