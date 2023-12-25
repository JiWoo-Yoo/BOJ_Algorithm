from collections import deque

def solution(n, edge):
    graph = {}
    for e in edge:
        a, b = e
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

    visited = [False] * (n + 1)
    distance = [0] * (n + 1)

    q = deque([1])
    visited[1] = True

    while q:
        node_a = q.popleft()
        for node_b in graph[node_a]:
            if not visited[node_b]:
                visited[node_b] = True
                distance[node_b] = distance[node_a] + 1
                q.append(node_b)

    max_distance = max(distance)
    count_max_distance = distance.count(max_distance)

    return count_max_distance
