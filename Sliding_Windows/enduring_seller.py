"""
We are given an array, best_seller, with the title of the most sold book for each day over a given period. 
We are also given a number k with 1 ≤ k ≤ len(sales).

We need to return whether there is any k-day period where every day has the same best-selling title.


Example 1:
best_seller = ["book3", "book1", "book3", "book3", "book2"]
k = 3

Output: False
No three consecutive days have the same best seller.

Example 2:
best_seller = ["book3", "book1", "book3", "book3", "book2"]
k = 2

Output: True
Days 3-4 have the same best seller "book3".

Example 3:
best_seller = ["book1", "book2", "book1"]
k = 2

Output: False
No two consecutive days have the same best seller.

Example 4:
best_seller = ["book1", "book1", "book1"]
k = 3

Output: True
The entire array has the same best seller.
Constraints:

The length of best_seller is at most 10^6
Each book title has length at most 100
1 <= k <= len(best_seller)
"""

def same_title(sales, k):
    l = 0
    r = 0

    seen = {}

    while r < len(sales):
        if sales[r] not in seen:
            seen[sales[r]] = 0
        seen[sales[r]] += 1
        r+=1
        print(seen)
        if r-l == k:
            if len(seen) == 1:
                return True
            
            seen[sales[l]] -= 1
            if seen[sales[l]] == 0:
                del seen[sales[l]]
            l += 1
    
    return False
    
best_seller = ["book3", "book1", "book3", "book3", "book2"]
k = 2

print(same_title(best_seller,k))