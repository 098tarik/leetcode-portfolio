"""
We are driving down a road with n rest stops between us and our destination. 
For each rest stop, our mapping software tells us how long of a detour it would be to stop there. 
We start before the first rest stop and our destination is past the last one.

We are given an array of n positive integers, times, indicating the delay incurred to stop at each rest stop. 
We are also given a positive integer k, indicating the number of consecutive rest areas we can skip.

If we don't want to go more than k rest stops without taking a break, what's the least amount of time we have to spend on detours?


Example 1:
times = [8, 1, 2, 3, 9, 6, 2, 4]
                        
k = 2
Output: 6.
The optimal rest stops are: [8, *1*, 2, *3*, 9, 6, *2*, 4].

base case:

    i >= n - k - 1
          8 -  8 - 5
    delay(n - (n - i)) = times[n - (n - i)]
          8 -  3
    delay(8 - (8 - 6)) = times[n - (n - i)]

    delay(8 - (8 - 7)) = times[n - (n - i)]

general case
    i >= n - k - 1:
        return times[i]
    if i in memo:
        return memo[i]
    i < n - k - 1
        current_time = time[i]
        min_time = 0
        for t in range(k):
            min(min_time, delay(i + t)
        
        delay(i) = current_time + min_time

return delay(0) 




Example 2:
times = [8, 1, 2, 3, 9, 6, 2, 4]
k = 3
Output: 4
The optimal rest stops are: [8, 1, *2*, 3, 9, 6, *2*, 4].

Example 3:
times = [10, 10]
k = 2
Output: 0
Constraints:

n is at least 0 and at most 1000.
times[i] is at least 1 and at most 1000.
k is at least 1 and at most 1000.
"""

def calculate_stops(times, k):
    memo = {}
    n = len(times)
    def min_stops(i):
        if i >= n:
            return 0
        if i >= n - k - 1:
            return times[i]  # We know min of future delays is 0

        if i in memo:
            return memo[i]
        
         # Choose to stop here + best of next k+1 positions
        current_time = times[i]
        min_future = float('inf')
        
        # Can skip to positions i+1, i+2, ..., i+k+1
        for next_stop in range(i + 1, i + k + 2):
            min_future = min(min_future, min_stops(next_stop))
        
        memo[i] = current_time + min_future
        return memo[i]
    
    result = float('inf')
    for start in range(k + 1):
        result = min(result, min_stops(start))
    return result

times = [8, 1, 2, 3, 9, 6, 2, 4]                 
k = 2

print(calculate_stops(times, k))

def run_tests():
  tests = [
      ([8, 1, 2, 3, 9, 6, 2, 4], 2, 6),
      ([8, 1, 2, 3, 9, 6, 2, 4], 3, 4),
      ([10, 10], 1, 10),
      ([10, 10], 2, 0),
      ([], 2, 0),
      ([5, 5, 5, 5, 5], 2, 5),
  ]

  for times, k, want in tests:
    got = calculate_stops(times, k)
    print(got, want)
    assert got == want, f"\nminivan_road_trip({times}, {k}): got: {
        got}, want: {want}\n"

run_tests()