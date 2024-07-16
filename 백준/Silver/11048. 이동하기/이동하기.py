# 아래로, 오른쪽, 오른쪽아래로 이동 가능
# 준규가 n, m으로 이동할 때 가져올 수 있는 사탕 개수의 최댓값
# (1, 1) -> (n, m) 까지의 가중치 합의 최대
# DP

n, m = map(int, input().split())
DP = []
for i in range(n):
    DP.append(list(map(int, input().split())))

for r in range(n):
    for c in range(m):
        if r == 0 and c == 0:
            continue
        elif r == 0 and c > 0:
            DP[r][c] = DP[r][c-1] + DP[r][c]
        elif r > 0 and c == 0:
            DP[r][c] = DP[r-1][c] + DP[r][c]
        else:
            DP[r][c] = max(DP[r][c-1], DP[r-1][c], DP[r-1][c-1]) + DP[r][c]

            
print(DP[n-1][m-1])