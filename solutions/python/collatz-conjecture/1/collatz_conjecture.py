def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number != 1:
        steps += 1
        even = number % 2 == 0
        if even:
            number = number / 2
        else:
            number = (number * 3) + 1
    return steps
