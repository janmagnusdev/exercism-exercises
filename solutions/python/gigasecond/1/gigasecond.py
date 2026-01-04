from datetime import timedelta

GIGASECOND = 10**9

def add(moment):
    delta = timedelta(seconds = GIGASECOND)
    return moment + delta
