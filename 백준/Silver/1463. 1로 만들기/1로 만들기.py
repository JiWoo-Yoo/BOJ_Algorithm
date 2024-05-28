# 연산 횟수의 최솟값
n = int(input())
dp = [0 for i in range(n+1)]

for i in range(2, n+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    
print(dp[n])