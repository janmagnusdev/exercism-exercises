import re
from itertools import starmap

def is_valid(isbn):

    # 9 digits plus one check character, sometimes seperated by hyphens
    isbn_re = re.compile("^\d-?\d{3}-?\d{5}-?[\d,X]$")
    if not isbn_re.match(isbn):
        return False
    
    base_isbn = isbn.replace("-", "")
    
    digits_list = list(base_isbn)
    
    if digits_list[9] == "X":
        digits_list[9] = 10
        
    digits_list = [int(digit) for digit in digits_list]

    def formula(digits_list):
        factors = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        factorized = starmap(lambda digit, factor: digit * factor, zip(digits_list, factors))
        return sum(factorized) % 11

    return formula(digits_list) == 0