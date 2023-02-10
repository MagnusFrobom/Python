from heapq import heappop, heappush

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (distance, current) = heappop(heap)
        if distance > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(heap, (distance, neighbor))
    return distances[end]

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}

print(dijkstra(graph, 'A', 'D')) # Output: 3
