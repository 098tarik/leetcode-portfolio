import heapq


def first_k(arr, k):
    res = []
    # heapq.heapify modifies the list in-place to satisfy the heap property
    # We create a copy so we don't scramble the original input array
    heap = arr[:]
    heapq.heapify(heap)
    
    for i in range(k):
        # heappop removes and returns the smallest element
        res.append(heapq.heappop(heap))
    return res

# Note: For this specific problem, Python also provides a helper:
# return heapq.nsmallest(k, arr)

arr = [1,4,2,8,10,5,2,1,3,9,11,11,27]
k = 5
result = first_k(arr,k)
print(result)