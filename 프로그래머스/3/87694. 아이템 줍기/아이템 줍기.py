from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 직접 맵 생성
    maps = [[-1 for i in range(51 * 2)] for _ in range(51 * 2)]
    
    # 좌표 입력(2배)
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # 사각형 채우기
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j <y2: # 내부는 0
                    maps[i][j] = 0
                elif maps[i][j] != 0: # 테두리는 1(다른사각형의 내부가 아닐때)
                    maps[i][j] = 1
    
    cx = characterX * 2
    cy = characterY * 2
    ix = itemX * 2
    iy = itemY * 2
    
    # BFS
    visited = [[1 for i in range(51 * 2)] for _ in range(51 * 2)]
    q = deque()
    q.append((cx, cy))
    while q:
        x, y = q.popleft()
        if x == ix and y == iy:
        	# 답 나누기 2 반환
            answer = visited[x][y] // 2
            break 
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]

            if maps[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                q.append((nx, ny))
    
    return answer