"""
You are given the adjacency list of an undirected graph, 
graph, a node index, start, and an array, queries, where each element is a node index.

Return an array with the same length as queries, 
where the i-th element is an array with the shortest path from start to queries[i].

If there is no path from start to queries[i], return an empty array for the i-th element.


Example 1:
graph = [
   [1],           # Node 0
   [0, 2, 5, 4],  # Node 1
   [1, 4, 5],     # Node 2
   [],            # Node 3
   [5, 2, 1],     # Node 4
   [1, 2, 4]      # Node 5
]
start = 0
queries = [1, 0, 3, 4]

Output: [[0, 1], [0], [], [0, 1, 4]]
Node 3 cannot be reached from node 0

Example 2:
graph = [
   [1],           # Node 0
   [0, 2],        # Node 1
   [1]            # Node 2
]
start = 0
queries = [1, 2]

Output: [[0, 1], [0, 1, 2]]

Example 3:
graph = [
   [1],           # Node 0
   [0],           # Node 1
   [3],           # Node 2
   [2]            # Node 3
]
start = 0
queries = [1, 2, 3]

Output: [[0, 1], [], []]
Can only reach node 1 from node 0
"""

from collections import deque


def shortest_path(graph, start, queries):
    q = deque()
    q.append(start)
    pred = {start: None}

    while q:
        node = q.popleft()
        for nbr in graph[node]:
            if nbr not in pred:
                pred[nbr] = node
                q.append(nbr)
    
    result = []
    for node in queries:
        if node not in pred:
            result.append([])
        else:
            path = []
            current = node
            while current is not None:
                path.append(current)
                current = pred[current]
            path.reverse()
            result.append(path)

    return result


    
graph = [
   [1],           # Node 0
   [0, 2, 5, 4],  # Node 1
   [1, 4, 5],     # Node 2
   [],            # Node 3
   [5, 2, 1],     # Node 4
   [1, 2, 4]      # Node 5
]

start = 0
queries = [1, 0, 3, 4]

print(shortest_path(graph,start,queries))