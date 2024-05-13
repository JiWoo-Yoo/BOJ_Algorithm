# 무방향 그리프의 연결 요소 개수 구하는 프로그램
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False for i in range(n+1)]

def dfs(v, graph, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i, graph, visited)
        cnt += 1 
    
print(cnt)
    
    
