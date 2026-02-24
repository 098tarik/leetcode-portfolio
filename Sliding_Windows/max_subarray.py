"""
Given a non-empty array arr of integers (which can be negative), 
find the non-empty subarray with the maximum sum and return its sum.


Example 1: arr = [1, 2, 3, -2, 1]
Output: 6. The subarray with the maximum sum is [1, 2, 3].

Example 2: arr = [1, 2, 3, -2, 7]
Output: 11. The subarray with the maximum sum is the whole array.
 
Example 3: arr = [1, 2, 3, -8, 7]
Output: 7. The subarray with the maximum sum is [7].

Example 4: arr = [-2, -3, -4]
Output: -2. The subarray cannot be empty.
Constraints:

1 <= len(arr) <= 10^5
Each element in arr is an integer between -10^6 and 10^6
"""

def subarray_sum(nums):
    l = 0
    r = 0
    if max(nums) <= 0:
        return max(nums)
    
    max_sum = 0
    sum = 0

    while r < len(nums):
        can_grow = sum + nums[r] > 0
        if can_grow:
            sum += nums[r]
            r += 1
            max_sum = max(sum, max_sum)
        else:
            sum = 0
            l = r + 1
            r = r + 1
    return max_sum

arr = [1, 2, 3, -2, 1]
print(subarray_sum(arr))
