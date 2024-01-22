# 참고: https://chldkato.tistory.com/60
from collections import deque

r, c = map(int, input().split())
g = []
for _ in range(r):
    g.append(input())

visited = [[False] * c for _ in range(r)]
q = deque()
v, k = 0, 0

# e s w n
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
  
def bfs(x, y):
    visited[x][y] = True
    v_cnt, k_cnt = 0, 0
    q.append([x, y])
    while q:
        x, y = q.popleft()
        if g[x][y] == 'v':
            v_cnt += 1
        elif g[x][y] == 'k':
            k_cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if g[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    if v_cnt >= k_cnt:
        k_cnt = 0
    else:
        v_cnt = 0
    return [v_cnt, k_cnt]

for i in range(r):
    for j in range(c):
        if g[i][j] != '#' and not visited[i][j]:
            v_cnt, k_cnt = bfs(i, j)
            v += v_cnt
            k += k_cnt
print(k, v)
