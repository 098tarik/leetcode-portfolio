import heapq

def k_most_played(arr, k):
    # arr is a list of tuples: (item_name, play_count)
    # To sort/heapify by the second value (play_count) in descending order:
    # We construct a heap of (-play_count, item_name)
    heap = [(-count,name) for name, count in arr]
    heapq.heapify(heap)
    
    result = []
    for _ in range(k):
        if not heap:
            break
        _, name = heapq.heappop(heap)
        # Convert back to (name, original_count)
        result.append(name)
    return result

songs = [["All the Single Brackets", 132],
         ["Oops! I Broke Prod Again", 274],
         ["Coding In The Deep", 146],
         ["Boolean Rhapsody", 193],
         ["Here Comes The Bug", 291],
         ["All About That Base Case", 291]]
k = 3

result = k_most_played(songs, k)
print(result)