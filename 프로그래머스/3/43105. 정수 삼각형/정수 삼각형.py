def solution(triangle):
    h = len(triangle) # 높이
    base = len(triangle[h-1]) # 밑변
    cnt = 0 # 역순 계산을 위한 index
    for i in range(h - 1, 0, -1):
        for j in range(base - cnt - 1):
            triangle[i-1][j] = max(triangle[i-1][j] + triangle[i][j], triangle[i-1][j] + triangle[i][j+1])
        cnt += 1
    answer = triangle[0][0]
    return answer