"""
We are given an array, best_seller, with the title of the most sold book for each day over a given period. 
We are also given a number k with 1 ≤ k ≤ len(sales).

We need to return whether there is any k-day period where each day has a different best-selling title.


Example 1:
best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"]
                                                     l                   r
k = 3

Output: True
There is a 3-day period without a repeated value: ["book2", "book3", "book4"]

Example 2:
best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4",
"book3"]
k = 4

Output: False
There are no 4-day periods without a repeated value

Example 3:
best_seller = ["book1", "book2", "book3"]
k = 3

Output: True
The entire array has no repeated values
"""

def best_book(sales, k):
    l = 0
    r = 0

    seen = {}

    while r < len(sales):
        if sales[r] not in seen:
            seen[sales[r]] = 0
        seen[sales[r]] += 1
        r += 1

        if r - l == k:
            if len(seen) == k:
                return True
            
            seen[sales[l]] -= 1
            if seen[sales[l]] == 0:
                del seen[sales[l]]
            l += 1
    
    return False

best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"]
k = 3

print(best_book(best_seller,k))