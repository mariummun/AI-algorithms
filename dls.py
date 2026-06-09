def dls(graph, node, goal, limit):
    if node == goal:
        return [node]

    if limit == 0:
        return None

    for neighbor in graph[node]:
        result = dls(graph, neighbor, goal, limit - 1)

        if result is not None:
            return [node] + result

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

start = 'A'
goal = 'F'
depth_limit = 2

path = dls(graph, start, goal, depth_limit)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not found within depth limit")