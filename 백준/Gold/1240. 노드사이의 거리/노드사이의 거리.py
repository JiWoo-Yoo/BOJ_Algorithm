# 그래프에서 노드 사이의 거리 구하기 - bfs 사용
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, e):
    q = deque([(s, 0)]) # 시작노드, 거리
    visited = [False] * (n + 1)
    visited[s] = True
    
    while q:
        now, dist = q.popleft()
        
        if now == e:
            return dist
        
        for i in range(1, n + 1):
            if graph[now][i] > 0 and not visited[i]:
                visited[i] = True
                q.append((i, dist + graph[now][i]))
    
    return -1

n, m = map(int, input().split())
graph = [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(n-1):
    a, b, d = map(int, input().split())
    graph[a][b] = d 
    graph[b][a] = d
    
for _ in range(m):
    u, v = map(int, input().split())
    print(bfs(u, v))