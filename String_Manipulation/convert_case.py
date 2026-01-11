
"""
Implement a function to_uppercase(char) that converts a lowercase
character to an uppercase character otherwise it does nothing
"""

def is_lowercase(char):
    return ord(char) >= ord('a') and ord(char) <= ord('z')

def to_uppercase(char):
    if is_lowercase(char):
        char = chr(ord(char) - ord('a') + ord('A'))
    else:
        return 
    
    return char
    