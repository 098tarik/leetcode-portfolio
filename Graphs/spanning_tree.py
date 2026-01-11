

def visit(graph, node, pred):
    for nei in graph[node]:
        if nei not in pred:
            pred[nei] = node
            visit(graph, nei, pred)

def is_spanning_tree(graph):
    pred = {0: None}  # Mark root with None parent
    result = []
    visited = set()

    visit(graph, 0, pred)

    for node in range(len(pred)):
        if pred[node] is not None:
            edge = [pred[node], node]
            result.append(edge)
    
    return result

graph = [
  [1, 2],
  [0, 2],
  [0, 1]
]

result = is_spanning_tree(graph)
print(result)