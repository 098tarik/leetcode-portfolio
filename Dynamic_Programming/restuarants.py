"""
We are doing a road trip and trying to plan where to stop to eat. 
There are n restaurants along the route. 
We are given an array, ratings, with the ratings of all the restaurants maximizing the sum of ratings of the places where we stop. The only constraint is that we don't want to stop at 2 consecutive restaurants, as we would be too full. Return the optimal sum of ratings.


Example 1:
ratings = [8, 1, 3, 9, 5, 2, 1]
Output: 19. The optimal restaurants are: [*8*, 1, 3, *9*, 5, *2*, 1]

base case:
        max_rating(n-1) = rating[n-1]
        max_rating(n-2) = rating[n-2]

general case:
        max_rating(i) = rating[i] + max(max_rating(i+1:k))


Example 2:
ratings = [8, 1, 3, 7, 5, 2, 4]
Output: 20. The optimal restaurants are: [*8*, 1, *3*, 7, *5*, 2, *4*].

Example 3:
ratings = []
Output: 0
Constraints:

n is at least 0 and at most 10^6.
ratings[i] is a floating-point number between 0 and 10 (inclusive).

T(N * (N - 1))
S(N)
"""

def calculate_ratings(ratings):
    memo = {}
    n = len(ratings)
    def max_ratings(i):
        if i >= n:
            return 0
        if i >= n - 2:
            return ratings[i]  # We know min of future delays is 0

        if i in memo:
            return memo[i]
        
         # Choose to stop here + best of next k+1 positions
        current_rating = ratings[i]
        max_rating = 0
        # Can skip to positions i+1, i+2, ..., i+k+1
        for next_rating in range(i + 2, n):
            max_rating = max(max_rating, max_ratings(next_rating))
        
        memo[i] = current_rating + max_rating
        return memo[i]
    
    result = 0
    for start in range(n):
        result = max(result, max_ratings(start))
    return result

ratings = [8, 1, 3, 7, 5, 2, 4]
print(calculate_ratings(ratings))

def run_tests():
  tests = [
    ([8, 1, 3, 9, 5, 2, 1], 19),
    ([8, 1, 3, 7, 5, 2, 4], 20),
    ([10, 10, 10, 10, 10], 30),
    ([], 0),
    ([5, 5, 5, 5, 5], 15),
  ]
  for ratings, want in tests:
    got = calculate_ratings(ratings)
    print(got, want)
    assert got == want, f"\nrestaurant_ratings({ratings}): got: {got}, want: {want}\n"

run_tests()