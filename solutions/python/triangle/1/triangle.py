from functools import reduce

def equilateral(sides):
    if not valid(sides):
        return False
    compare = sides[0]
    return all(x == compare for x in sides)

def valid(sides):
    if all(x == 0 for x in sides):
        return False
    for x in sides:
        others = sides.copy()
        others.remove(x)
        sum = reduce(lambda x, y: x + y, others)
        if x > sum:
            return False
    return True
        

def isosceles(sides):
    if not valid(sides):
        return False
    same_sides = 1
    seen_values = []
    for x in sides:
        if x in seen_values:
            same_sides += 1
        seen_values.append(x)
    return same_sides >= 2


def scalene(sides):
    if not valid(sides):
        return False
    for x in sides:
        copied = sides.copy()
        copied.remove(x)
        if x in copied:
            return False
    return True
