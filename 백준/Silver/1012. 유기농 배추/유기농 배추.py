# 배추들이 모인 곳에는 배추흰지렁이가 한마리 ok
# 밭을 돌면서 배추가 있는 곳에 bfs
# 1: 배추 심어짐, 2: 배추 심었으면서 visited
from collections import deque
def bfs(i, j):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx <= n and 0 <= ny <= m:
                if field[nx][ny] == 1:
                    q.append((nx, ny))
                    field[nx][ny] = 2
                    
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
t = int(input())
for _ in range(t):
    worms = 0
    m, n, k = map(int, input().split())
    field = [[0 for a in range(m+1)] for b in range(n+1)]
    for i in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1 # 배추 심기

    # 전체 밭을 돌아가면서 배추 탐색
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1: # 배추가 있다
                bfs(i, j) # 인접한 배추 탐색
                worms += 1
                        
    print(worms)
        
