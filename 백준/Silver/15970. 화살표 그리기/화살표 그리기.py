# p -> q(q는 p와 같은 색이며 가장 가까운 점.)
# 흰: 1, 검: 2
# 모든 화살표들의 길이의 합 구하기
n = int(input())
coord = []
for _ in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))
coord.sort()

# 순차탐색 하면서 각각의 화살표 구하기
total = 0
for i in range(n):
    rarr = float('inf')
    larr = float('inf')
    for j in range(i+1, n): # 오른쪽으로 찾기
        if coord[j][1] == coord[i][1]:
            rarr = coord[j][0] - coord[i][0]
            break
    for k in range(i-1, -1, -1): # 왼쪽으로 찾기
        if coord[k][1] == coord[i][1]:
            larr = coord[i][0] - coord[k][0]
            break
    total += min(rarr, larr)
print(total)
