"""
Given the adjacency list of a non-empty directed graph, graph, return whether it is strongly connected.

A directed graph is strongly connected if every node can reach every other node 
(in a directed graph, it is possible that node1 can reach node2 but not the other way around).

Below is an image of strongly connected, weakly connected, and disconnected directed graphs. 
A directed graph is weakly connected if it would be connected if edges didn't have directions.

Strongly Connected Graph

Example 1:
graph = [
  [1, 3],    # Node 0
  [2],       # Node 1
  [0],       # Node 2
  [2]        # Node 3
]

Output: True
Left graph in the image above

Example 2:
graph = [
  [1, 2, 3], # Node 0
  [2],       # Node 1
  [],        # Node 2
  [2]        # Node 3
]

Output: False
Middle graph in the image above
Node 2 cannot reach node 0, among others

Example 3:
graph = [
  [1],       # Node 0
  [0],       # Node 1
  [3],       # Node 2
  [2]        # Node 3
]

Output: False
Right graph in the image above
Node 0 cannot reach node 3, among others
Constraints:

1 ≤ graph.length ≤ 1000
graph[i].length < 1000
0 ≤ graph[i][j] < graph.length
The adjacency list is properly formatted, with no parallel edges or self-loops
The graph is directed
"""

def strongly_connected(graph):
    n = len(graph)

    def dfs(adj, node, seen):
        seen.add(node)
        for nbr in adj[node]:
            if nbr not in seen:
                dfs(adj, nbr, seen)
        return seen

    # 1) Check all nodes reachable from node 0
    if len(dfs(graph, 0, set())) != n:
        return False

    # 2) Build reversed graph
    reversed_graph = [[] for _ in range(n)]
    for node in range(n):
        for nbr in graph[node]:
            reversed_graph[nbr].append(node)
    print(reversed_graph)

    # 3) Check all nodes reachable from node 0 in reversed graph
    return len(dfs(reversed_graph, 0, set())) == n

graph = [
  [1, 2, 3], # Node 0
  [2],       # Node 1
  [],        # Node 2
  [2]        # Node 3
]

print(strongly_connected(graph))