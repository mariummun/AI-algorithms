import heapq

def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])]  # (cost, current_node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (cost + edge_cost,
                     neighbor,
                     path + [neighbor])
                )

    return None

# Graph representation:
# ('neighbor', cost)

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 10)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

start = 'A'
goal = 'E'

result = uniform_cost_search(graph, start, goal)

if result:
    path, cost = result
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")