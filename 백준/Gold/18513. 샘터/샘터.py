from collections import deque

n, k = map(int, input().split())
sam_pos = list(map(int, input().split()))
visited = set()

q = deque()

for sam in sam_pos: # 샘을 큐에 추가
    q.append((sam, 1)) # 위치, 불행도
    visited.add(sam)
    
answer = 0 # 불행도 합
built = 0 # 현재까지 지어진 집의 수

while q:
    s, b = q.popleft()
    for d in [1, -1]: # 왼쪽, 오른쪽
        nx = d + s # 집을 지을 위치
        if nx in visited: # 이미 방문한곳이면
            continue
        visited.add(nx) # 아니면 방문
        answer += b # 불행도 추가
        built += 1
        q.append((nx, b + 1))
        if built == k:
            q = []
            break
            
print(answer)
            
            
        
