from typing import List, Tuple

def can_color_graph(n: int, edges: List[Tuple[int, int]], k: int) -> bool:
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Heuristic: color high-degree nodes first (shrinks search a lot)
    order = sorted(range(n), key=lambda v: len(graph[v]), reverse=True)

    color = [0] * n  # 0 = uncolored, otherwise 1..k

    def is_valid_color(v: int, c: int) -> bool:
        for nei in graph[v]:
            if color[nei] == c:
                return False
        return True

    def dfs(i: int) -> bool:
        # If we've colored all vertices in 'order', we've found a solution
        if i == n:
            return True

        v = order[i]

        # Try each color (each one is a child in the decision tree)
        for c in range(1, k + 1):
            if is_valid_color(v, c):
                color[v] = c
                if dfs(i + 1):
                    return True
                color[v] = 0  # backtrack

        # No color worked for this vertex => dead end leaf
        return False

    return dfs(0)


# --- Example usage ---
if __name__ == "__main__":
    # Triangle graph: needs 3 colors
    n = 3
    edges = [(0, 1), (1, 2), (0, 2)]
    print(can_color_graph(n, edges, k=2))  # False
    print(can_color_graph(n, edges, k=3))  # True
