"""
arr = [5,1,-2,7,-14,-4]


"""

def subset_sum(arr):
    # To find strict subsets summing to 0, we generally want non-empty subsets.
    # If empty subsets are allowed, the answer is always True (sum is 0).
    
    def backtrack(index, current_sum, count):
        # Base case: if we found a non-empty subset summing to 0
        if count > 0 and current_sum == 0:
            return True
        
        # Base case: if we've gone through all elements
        if index == len(arr):
            return False
        
        # Choice 1: Include the current element
        if backtrack(index + 1, current_sum + arr[index], count + 1):
            return True
            
        # Choice 2: Exclude the current element
        if backtrack(index + 1, current_sum, count):
            return True
            
        return False

    return backtrack(0, 0, 0)


arr = [5,1,-2,7,-14,-2]
if subset_sum(arr):
    print("valid")
else:
    print("invalid")
