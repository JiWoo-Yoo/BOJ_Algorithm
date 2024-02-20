n, k = map(int, input().split())
# 0~n까지의 정수 중 k개를 더해 그 합이 n이 되는
# 경우의 수 구하기
# DP
DP = [[0 for i in range(n+1)] for j in range(k+1)]

# 점화식(DP[k][n] == Σ(DP[k-1][n-L]) 코드
for i in range(n + 1):
    DP[1][i] = 1
    
for i in range(1, k + 1):
    for j in range(n + 1):
        for l in range(j + 1):
            DP[i][j] += DP[i-1][j-l]

print(DP[k][n] % 1000000000)