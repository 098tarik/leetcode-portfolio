"""
A valley-shaped array is an array of integers such that:

It can be split into a non-empty prefix and a non-empty suffix,
The prefix is sorted in decreasing order,
The suffix is sorted in increasing order,
All the elements are unique.
Given a valley-shaped array, arr, return the smallest value.


Example 1: arr = [6, 5, 4, 7, 9]
Output: 4

Example 2: arr = [5, 6, 7]
Output: 5. The prefix sorted in decreasing order is just [5].

Example 3: arr = [7, 6, 5]
Output: 5. The suffix sorted in increasing order is just [5].
Constraints:

2 ≤ arr.length ≤ 10^6
-10^9 ≤ arr[i] ≤ 10^9
"""

def is_before(arr, i):
    return arr[i] > arr[i + 1]

def valley_bottom(arr):

    if not arr:
        return -1
    
    l = 0
    r = len(arr) - 1

    if is_before(arr, r - 1):
        return arr[r]
    if not is_before(arr, l):
        return arr[l]
    
    while r - l > 1:
        mid = (r - l) // 2

        if is_before(arr, mid):
            l = mid
        else:
            r = mid

    return arr[r]

arr = [3, 2, 4]
print(valley_bottom(arr))

