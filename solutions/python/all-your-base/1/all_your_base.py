def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(map(lambda d: not (0 <= d < input_base), digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if len(digits) < 1 or (set(digits) == {0}):
        return [0]


    
    reversed = digits[::-1]
    value_in_base_ten = 0
    for index, digit in enumerate(reversed):
        value_in_base_ten += digit * input_base ** index 



    # Divide the original base 10 number by the target base \(B\).
    # Record the remainder. This will be the first (rightmost), or least significant, digit of your new number.
    # Take the quotient (the whole number result of the division) and divide it by the base \(B\) again.
    # Repeat this process, recording the remainder at each step, until the quotient becomes zero.
    # The final result is obtained by writing down the remainders from bottom to top (the last remainder is the most significant digit). 
    quotient = value_in_base_ten
    out_digits = []
    i = 0
    while quotient > 0 and i < 100:
        result, remainder = divmod(quotient, output_base)
        quotient = result
        out_digits.append(remainder)
        i += 1
    out_digits = out_digits[::-1]
    return out_digits
