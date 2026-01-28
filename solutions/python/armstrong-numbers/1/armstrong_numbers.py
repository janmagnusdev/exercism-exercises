def is_armstrong_number(number):
    no_of_digits = len(str(number))
    armstrong_value = sum([int(digit) ** no_of_digits for digit in str(number)])
    return armstrong_value == number

