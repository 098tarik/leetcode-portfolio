"""
Validate Undirected Graph

Given an adjacency list representation of a graph, determine whether it's a valid undirected graph.

A valid undirected graph must satisfy:
1. Every node is between 0 and V-1 (where V is the number of vertices)
2. No self-loops: edges connecting a node to itself
3. No parallel edges: two edges connecting the same two nodes
4. Symmetry: If node1 appears in graph[node2], then node2 must also appear in graph[node1]
"""



def is_valid_undirected_graph(graph):
    """
    Validate whether the given adjacency list represents a valid undirected graph.
    
    Args:
        graph: List of lists where graph[i] contains the neighbors of node i
        
    Returns:
        bool: True if the graph is valid, False otherwise
    """
    # TODO: Implement the validation logic here
    
    size = len(graph)
 
    if not graph:
        return True
    
    for node in range(size):
        seen = set()
        for nei in graph[node]:
            if nei < 0 or nei > size:
                return False
            if nei == node:
                return False
            if nei in seen:
                return False
            seen.add(nei)
    
    edges = set()
    for node1 in range(size):
        for node2 in graph[node1]:
            edge = (min(node1, node2), max(node1, node2))
            if edge in edges:
                edges.remove(edge)
            else:
                edges.add(edge)
        
    return len(edges) == 0

if (is_valid_undirected_graph([[1, 2], [0, 2], [0, 1]])):
    print("valid")
else:
    print("invalid")
            


