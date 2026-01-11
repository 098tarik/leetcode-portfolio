"""
We are given an array of letters, arr, with a length, n, which is a multiple of 3. The goal is to modify arr in place to move the prefix of length n/3 to the end and the suffix of length 2n/3 to the beginning.


Example 1:
Input: arr = ['b', 'a', 'd', 'r', 'e', 'v', 'i', 'e', 'w']
Output: ['r', 'e', 'v', 'i', 'e', 'w', 'b', 'a', 'd']
Explanation: The first third (bad) moves to the end, while the rest (review)
stays in order.

Example 2:
Input: arr = ['a', 'b', 'c']
Output: ['b', 'c', 'a']

Example 3:
Input: arr = []
Output: []
Constraints:

The length of arr is divisible by 3
0 ≤ arr.length ≤ 10^6
arr[i] is a letter

Input: arr = ['b', 'a', 'd', 'r', 'e', 'v', 'i', 'e', 'w']
                              l                            
                                            r

Input: arr = ['i', 'e', 'w', 'r', 'e', 'v', 'b', 'a', 'd']
               r               l
"""

def prefix_suffix_swap(arr):
    if len(arr) == 0:
        return

    n = len(arr)

    # Reverse the whole array
    l, r = 0, n - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    # Reverse the last n/3 elements
    l, r = 2 * n // 3, n - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    # Reverse the first 2n/3 elements
    l, r = 0, (2 * n // 3) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

arr = ['b', 'a', 'd', 'r', 'e', 'v', 'i', 'e', 'w']
prefix_suffix_swap(arr)
print(arr)
