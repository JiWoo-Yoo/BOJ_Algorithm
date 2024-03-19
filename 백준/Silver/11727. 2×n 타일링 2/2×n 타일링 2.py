n = int(input())
max_v = 1000

dp = [0 for _ in range(max_v+1)]

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-2]
    
print(dp[n] % 10007)
