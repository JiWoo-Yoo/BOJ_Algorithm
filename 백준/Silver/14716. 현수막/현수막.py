import sys
sys.setrecursionlimit(100000)

m, n = map(int, input().split())
banner = []
for i in range(m):
    banner.append(list(map(int, input().split())))

# 1시방향부터 시계방향으로
dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

def dfs(graph, r, c):
    graph[r][c] = 2 # visited
    for d in range(8):
        y, x = r+dy[d], c+dx[d]
        if 0 <= y < len(graph) and 0 <= x < len(graph[0]) and graph[y][x] == 1:
            dfs(graph, y, x)
        
cnt = 0
for i in range(m):
    for j in range(n):
        if banner[i][j] == 1:
            dfs(banner, i, j)
            cnt += 1

print(cnt)