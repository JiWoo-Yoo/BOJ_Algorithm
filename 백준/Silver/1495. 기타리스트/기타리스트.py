# 곡의 개수, 시작 볼륨, 볼륨최댓값
n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)] # 곡마다 가능한 볼륨
dp[0][s] = 1
for i in range(1, n + 1): # i번 곡 전에 볼륨 조정
    for j in range(m + 1):
        if dp[i - 1][j] == 1:
            if j - v[i - 1] >= 0:
                dp[i][j - v[i - 1]] = 1
            if j + v[i - 1] <= m:
                dp[i][j + v[i - 1]] = 1
    
answer = -1
for i in range(m + 1):
    if dp[n][i] == 1:
        answer = i
print(answer)
