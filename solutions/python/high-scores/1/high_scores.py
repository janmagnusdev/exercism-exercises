"""
Docstring
"""


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    found = []
    i = 3
    while len(scores) > 0 and i > 0:
        maxf = max(scores)
        scores.pop(scores.index(maxf))
        found.append(maxf)
        i -= 1
    return found
