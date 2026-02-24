"""
Given the array sales and a number k with 1 ≤ k ≤ len(sales), find the most sales in any k-day period.

Return the first day of that period (days start at 0).
If there are multiple k-day periods with the most sales, return the first day of the first one.


Example 1: sales = [8, 1, 3, 7], k = 2
Output: 2
The subarray of length 2 with maximum sum is [3, 7], which starts at index 2.

Example 2: sales = [5, 10, 15, 5], k = 1
Output: 2
The day with most sales is day 2 with 15 sales.

Example 3: sales = [1, 2, 3], k = 3
Output: 0
The only valid period is the entire array.
Constraints:

The length of sales is at most 10^6
Each element in sales is a non-negative integer less than 10^3
1 ≤ k ≤ len(sales)
"""

def best_day(sales, k):

    l = 0
    r = 0

    max_sales = 0
    sale_sum = 0
    best_day = 0

    while r < len(sales):
        sale_sum += sales[r]
        r += 1

        if r - l == k:
            if sale_sum > max_sales:
                max_sales = sale_sum
                best_day = l
            sale_sum -= sales[l]
            l += 1

    return best_day

sales = [1, 2, 3]
k = 3

print(best_day(sales,k))