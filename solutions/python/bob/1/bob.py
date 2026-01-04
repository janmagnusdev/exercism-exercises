"""
A program which imitates bob.
"""
ANSWER_YELL = "Whoa, chill out!"
ANSWER_QUESTION = "Sure."
ANSWER_YELLED_QUESTION = "Calm down, I know what I'm doing!"
ANSWER_NOTHING = "Fine. Be that way!"
ANSWER_ELSE = "Whatever."

def response(hey_bob):
    """
    Checks the said sentence for different cases and simulates
    bobs response.
    """
    hey_bob = hey_bob.strip()
    if isQuestion(hey_bob):
        if isYelling(hey_bob):
            return ANSWER_YELLED_QUESTION
        return ANSWER_QUESTION
    if isYelling(hey_bob):
        return ANSWER_YELL
    if isNothing(hey_bob):
        return ANSWER_NOTHING
    return ANSWER_ELSE

def isQuestion(sent):
    return sent.endswith("?")

def isYelling(sent):
    return sent.isupper()

def isNothing(sent):
    return sent == "" or sent.isspace()

