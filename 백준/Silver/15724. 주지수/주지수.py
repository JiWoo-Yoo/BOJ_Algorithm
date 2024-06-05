# DP, 누적 합 안하면 시간초과

n, m = map(int, input().split())
whole = []
dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

for i in range(n):
    whole.append(list(map(int, input().split())))
    
# DP[i]는 윗항 + 왼쪽항 - 왼쪽위항 + 현재위치
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + whole[i-1][j-1]
    
k = int(input())

for i in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    total = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
    print(total)