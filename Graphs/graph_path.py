

def visit(graph, node1, node2, seen, path, result):
    if (node1 == node2):
        result[:] = path

    for nei in graph[node1]:
        if not nei in seen:
            seen.add(nei)
            path.append(nei)
            visit(graph, nei, node2, seen, path, result)
            path.pop()
            seen.remove(nei)

    


def does_graph_path_exist(graph, node1, node2):
    """
    Given the adjacency list of an undirected graph, graph, and two distinct nodes, node1 and node2, return a simple path from node1 to node2.

    A simple path does not repeat any nodes. Return an empty array if there is no path from node1 to node2.
    """
    # TODO: Implement the validation logic here
    seen = {node1}
    result = []
    path = [node1]

    visit(graph, node1, node2, seen, path, result)

    return result

graph = [
  [1],
  [0, 2],
  [1]
]
node1 = 0
node2 = 2

result = does_graph_path_exist(graph, node1, node2)
print(result)
