"""
You are given two non-empty arrays of integers, sorted_arr and unsorted_arr. 
The first one is sorted, but the second is not. The goal is to find one element from each array with sum 0. 
If you can find them, return an array with their indices, starting with the element in sorted_arr. 
Otherwise, return [-1, -1]. Use O(1) extra space and do not modify the input.


Example 1:
               0   1   2  3  4  5  6
sorted_arr = [-5, -4, -1, 4, 6, 6, 7]
              l                    
                           r        r

                          


              
unsorted_arr = [-3, 7, 18, 4, 6]
Output: [1, 3]
Explanation: We can use -4 from the sorted array and 4 from the unsorted array.

Example 2:
sorted_arr = [1, 2, 3]
unsorted_arr = [1, 2, 3]
Output: [-1, -1]
Explanation: No pair of elements sums to 0.

Example 3:
sorted_arr = [-2, 0, 1, 2]
unsorted_arr = [0, 2, -2, 4]
Output: [0, 1]
Explanation: We can use -2 from the sorted array and 2 from the unsorted array.
"""

def two_array_two_sum(sorted_arr, unsorted_arr):

  def binary_search(arr, target):

    def is_before(i):
      return arr[i] < target

    l, r = 0, len(arr) - 1
    if arr[l] > target or arr[r] < target:
      return -1
    if arr[l] == target:
      return l

    while r - l > 1:
      mid = (l + r) // 2
      if is_before(mid):
        l = mid
      else:
        r = mid

    if arr[r] == target:
      return r
    return -1

  for i, val in enumerate(unsorted_arr):
    idx = binary_search(sorted_arr, -val)
    if idx != -1:
      return [idx, i]
  return [-1, -1]