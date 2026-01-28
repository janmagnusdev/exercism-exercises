def is_isogram(string):
    chars = {}
    for char in string:
        char = char.lower()
        count = chars.get(char, 0)
        count += 1
        if count > 1 and char not in [" ", "-"]: 
            return False
        chars[char] = count
    return True