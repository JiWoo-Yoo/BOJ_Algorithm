import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
can_jump = list(map(int, input().split()))
start = int(input())

# 1 2 3 4 ... n 
# 현재 위치가 주어졌을 때, 영우가 방문 가능한 돌들의 개수 
# : 각 돌로부터 출발해서 도착할 수 있는 돌들의 경우의 수 구하기
# 왼쪽이나 오른쪽으로 점프할 수 있기 때문에 두 가지 경우씩 한번에 살피기위해 BFS

q = deque([start])
visited = [False for _ in range(n+1)]
cnt = 0

while q:
    now_stone = q.popleft()
    visited[now_stone] = True
    cnt += 1
    
    next_left_stone = now_stone - can_jump[now_stone - 1]
    next_right_stone = now_stone + can_jump[now_stone - 1]
    
    if 1 <= next_left_stone <= n: # 범위 내
        if not visited[next_left_stone]:
            q.append(next_left_stone)
    if 1 <= next_right_stone <= n: # 범위 내
        if not visited[next_right_stone]:
            q.append(next_right_stone)
        
print(cnt)