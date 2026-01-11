"""
Without using a built-in string join method, implement a join(arr,s)
method, which receives an array of strings `arr` and a string `s`
and returns a single string consistring of the strings in arr"""


def join(arr, s):
    if not arr:
        return ""
    
    result = arr[0]
    for index in range(1, len(arr)):
        result += s + arr[index]
    
    return result 

