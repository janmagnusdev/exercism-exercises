import re
from itertools import starmap

def is_valid(isbn):

    # validate 9 digits plus one check character seperated by hyphens; regex?
    isbn_re = re.compile("^\d-?\d{3}-?\d{5}-?[\d,X]$")
    if not isbn_re.match(isbn):
        # invalid isbn given
        return False
    
    # remove hyphens from isbn
    base_isbn = isbn.replace("-", "")
    # get each number individually
    digits_list = list(base_isbn)
    # get the last number as well - if it is X, set to 10
    if digits_list[9] == "X":
        digits_list[9] = 10
    # convert the numbers to ints
    digits_list = [int(digit) for digit in digits_list]

    def formula(digits_list):
        factors = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        factorized = starmap(lambda digit, factor: digit * factor, zip(digits_list, factors))
        return sum(factorized) % 11

    return formula(digits_list) == 0
    
    pass