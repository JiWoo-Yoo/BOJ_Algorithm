# t(n) = t(0) * t(n-1) + t(1) * (n-2) + ... + t(n-1) * t(0)일 때
# t(n)을 출력하는 프로그램

n = int(input())

dp = [0 for i in range(36)]

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5
if n > 3:
    for i in range(4, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]

print(dp[n])