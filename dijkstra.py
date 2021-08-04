# encoding=utf8

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}
}


unSelected = {node:None for node in nodes}
resultSet = {}
current = 'A'
dist = {
    current: 0
}


while unSelected:
    for neighbour, d in distances[current].items():
        if neighbour in resultSet:
            continue
        if dist.get(neighbour) is None or d + dist[current] < dist[neighbour]:
            dist[neighbour] = d+dist[current]

    resultSet[current] = 1
    del unSelected[current]

    next_node = None
    for k, _ in unSelected.items():
        if k not in dist:
            continue
        if not next_node:
            next_node = k
            continue
        if dist[k] < dist[next_node]:
            next_node = k
    current = next_node

print(dist)



def floyd(graph):
    length = len(graph)
    for k in range(0, length):
        for i in range(0, length):
            for j in range(0, length):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    return graph

