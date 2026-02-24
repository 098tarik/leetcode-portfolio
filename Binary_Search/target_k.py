"""
Given a sorted array of integers, arr, a target value, target, and a positive integer, 
k, return whether the number of occurrences of the target in the array is a multiple of k.


Example 1: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 3
Output: True. 2 occurs 6 times, which is a multiple of 3.

Example 2: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 2, k = 4
Output: False. 2 occurs 6 times, which is not a multiple of 4.

Example 3: arr = [1, 2, 2, 2, 2, 2, 2, 3], target = 4, k = 3
Output: True. 4 occurs 0 times, and 0 is a multiple of any number.
Constraints:

1 ≤ arr.length ≤ 10^6
-10^9 ≤ arr[i], target ≤ 10^9
1 ≤ k ≤ 10^6
arr is sorted in ascending order

"""

def find_multiple(arr, target, k):
    def is_before_end(index):
        return arr[index] <= target
    def is_before_start(index):
        return arr[index] < target
    
    l = 0
    r = len(arr) - 1

    if not is_before_end(l):
        return True
    elif is_before_start(r):
        return True
    
    while r - l > 1:
        mid = (r + l) // 2
        if is_before_start(mid):
            l = mid
        else:
            r = mid
    start_pos = l if not is_before_start(l) else l + 1

    l = 0
    r = len(arr) - 1

    while r - l > 1:
        mid = (r + l) // 2
        if is_before_end(mid):
            l = mid
        else:
            r = mid
    end_pos = r if is_before_end(r) else l

    return (end_pos - start_pos + 1) % k == 0

arr = [1, 2, 2, 2, 2, 2, 2, 3]
target = 2
k = 3

print(find_multiple(arr,target,k))


def run_tests():
  tests = [
      # Example 1
      ([1, 2, 2, 2, 2, 2, 2, 3], 2, 3, True),
      # Example 2
      ([1, 2, 2, 2, 2, 2, 2, 3], 2, 4, False),
      # Example 3: 0 occurrences, 0 is multiple of any number
      ([1, 2, 2, 2, 2, 2, 2, 3], 4, 3, True),
      # Example 4
      ([1, 1, 2, 2, 2], 1, 3, False),
      # single occurrence, at the start
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 2, False),
      # single occurrence, at the end
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, 2, False),
      # single occurrence, in the middle
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9, 2, False),
      # smaller than any elements
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0, 2, True),
      # larger than any elements
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 1, True),
      ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 20, 2, True),
      # Edge case - every occurrence is target
      ([5, 5, 5, 5, 5], 5, 5, True),
      ([5, 5, 5, 5, 5], 5, 3, False),
  ]
  for arr, target, k, want in tests:
    got = find_multiple(arr, target, k)
    assert got == want, f"\ntarget_count_divisible_by_k({arr}, {target}, {k}): got: {
        got}, want: {want}\n"

run_tests()