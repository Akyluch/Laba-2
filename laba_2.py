import heapq

INF = float('inf')

def dijkstra(graph, start):
    n = len(graph)
    dist = [INF] * n
    visited = [False] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        (d, u) = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, weight in enumerate(graph[u]):
            if weight is None:
                continue
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
    return dist

with open('graph_3.txt', 'r') as f:
    graph = []
    for line in f:
        row = [int(x) if int(x) != 0 else None for x in line.split()]
        graph.append(row)

n = len(graph)

for i in range(n):
    distances = dijkstra(graph, i)
    print(f'Найкоротша відстань від вершин {i}: {distances}')
