

def visit(graph, node, pred, found_cycle):

    for nei in graph[node]: # 2, 0, 2
        if nei not in pred: # false, false, true
            pred[nei] = node
            visit(graph, nei, pred, found_cycle)
        elif nei != pred[node]:
            found_cycle = True





def is_tree(graph):
    """
    Given the adjacency list of an undirected graph, graph, and two distinct nodes, node1 and node2, return a simple path from node1 to node2.

    A simple path does not repeat any nodes. Return an empty array if there is no path from node1 to node2.
    """
    # TODO: Implement the validation logic here
    pred = {0: None}
    found_cycle = False
    visit(graph, 0, pred, found_cycle)

    
    return not found_cycle and len(pred) == len(graph)

graph = [
  [2],           # Node 0
  [2, 5],        # Node 1
  [0, 1, 3, 4],  # Node 2
  [2],           # Node 3
  [2],           # Node 4
  [1]            # Node 5
]

if (is_tree(graph)):
    print("valid")
else:
    print("invalid")

