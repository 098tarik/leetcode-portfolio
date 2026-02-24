"""
Given the array sales, where sales[i] is the number of sales on the i-th day, 
find the longest sequence of days alternating between good days and bad days.

A good day is a day with at least 10 sales. A bad day is a day with fewer than 10 sales.


Example 1: sales = [8, 9, 20, 0, 9]
                       l
                              r
Output: 3. The only good day is day 2, so the subarray [9, 20, 0] alternates
from bad to good to bad.

Example 2: sales = [0, 0, 0]
Output: 1. Every day is bad, so we cannot find any pair of consecutive days
that alternate.

Example 3: sales = [5, 10, 5, 10]
Output: 4. The entire array alternates between bad and good days.
Constraints:

0 <= len(sales) <= 10^5
0 <= sales[i] <= 10^3
"""

def alternate_array(nums):
    if not nums:
        return 0
    
    max_seq = 1
    seq_len = 1
    r = 1

    while r < len(nums):
        can_grow = False

        if nums[r] < 10 and nums[r - 1] >= 10:
            can_grow = True
        elif nums[r] >= 10 and nums[r - 1] < 10:
            can_grow = True

        if can_grow:
            seq_len += 1
            max_seq = max(seq_len, max_seq)
        else:
            seq_len = 1

        r += 1

    return max_seq

sales = [5, 10, 5, 10]
print(alternate_array(sales))