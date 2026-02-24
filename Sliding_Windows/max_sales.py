"""
Imagine that you have a little bookstore. 
We have an array, projected_sales, with the projected number of sales per day in the future.

We are trying to pick k days for an advertising campaign, 
which we expect to boost the sales on those specific days by 5 sales. 
You cannot boost the same day more than once.

If we pick the days for the advertising campaign correctly, 
what is the maximum number of consecutive good days in a row we can get?

A good day is a day with at least 10 sales.


Example 1: projected_sales = [8, 4, 8], k = 3
                                 l
Output: 1. We can boost all 3 days, resulting in [13, 9, 13] projected sales.
The max consecutive good days is 1.

Example 2: projected_sales = [10, 5, 8], k = 1
Output: 2. We should boost day 1, resulting in [10, 10, 8] projected sales.

Example 3: projected_sales = [8, 8, 8], k = 3
Output: 3. We can boost all days to reach 13 sales each.
Constraints:

0 <= len(projected_sales) <= 10^5
0 <= projected_sales[i] <= 10^3
0 <= k <= len(projected_sales)
"""

def max_days(sales, k):
    if not sales:
        return 0

    l = 0
    max_good = 0
    boosts_used = 0

    for r in range(len(sales)):
        # Day can't be made good even with a boost (< 5 + 5 = 10)
        if sales[r] + 5 < 10:
            # Reset: skip past this day
            l = r + 1
            boosts_used = 0
            continue

        # Day needs a boost (5 <= sales[r] < 10)
        if sales[r] < 10:
            boosts_used += 1

        # If we've used too many boosts, shrink from the left
        while boosts_used > k:
            if sales[l] < 10:
                boosts_used -= 1
            l += 1

        max_good = max(max_good, r - l + 1)

    return max_good