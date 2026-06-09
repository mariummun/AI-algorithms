def dls(graph, node, goal, limit):
    if node == goal:
        return [node]

    if limit == 0:
        return None

    for neighbor in graph[node]:
        result = dls(graph, neighbor, goal, limit - 1)

        if result:
            return [node] + result

    return None


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, start, goal, depth)

        if result:
            return result

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

path = ids(graph, 'A', 'F', 10)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not found")