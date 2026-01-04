from string import ascii_lowercase

def is_pangram(sentence):
    dict = {i: False for i in ascii_lowercase}
    for char in sentence.lower():
        dict[char] = True
    return all(dict.values())
