
"""
Implement a function `is_alphanumeric(c)` that returns whether 
a character char is a lowercase or uppercase or digit character
"""
def is_lowercase(char):
    return ord(char) >= ord('a') and ord(char) <= ord('z')

def is_uppercase(char):
    return ord(char) >= ord('A') and ord(char) <= ord('Z')


def is_digit(char):
    return ord(char) >= ord('0') and ord(char) <= ord('9')

def is_alphanumeric(char):
    return is_lowercase(char) or is_uppercase(char) or is_digit(char)