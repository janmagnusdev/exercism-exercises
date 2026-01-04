"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
NOTHING = -1
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if is_equal(list_one, list_two):
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_superlist(list_one, list_two):
        return SUPERLIST
    if is_unequal(list_one, list_two):
        return UNEQUAL
    return NOTHING

def is_sublist(one, two):
    result = False
    a_length = len(one)
    b_length = len(two)
    for i, x in enumerate(two):
        possible_sublist = two[i:(i + a_length)]
        if is_equal(one, possible_sublist):
            result = True
    return result

def is_superlist(one, two):
    return is_sublist(two, one)

def is_equal(one, two):
    if len(one) != len(two):
        return False
    result = True
    for i, x in enumerate(one):
        try:
            if two[i] != x:
                result = False
        except IndexError:
            result = False
            break
    return result

def is_unequal(one, two):
    return not is_equal(one, two)