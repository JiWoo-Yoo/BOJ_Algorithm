# n자리 이친수의 개수 => DP
import sys
input = sys.stdin.readline

n = int(input())

# 이친수는 10으로 시작하면서, 11이 들어가지 않음.
# 즉, n자리 이친수의 개수: n-1자리 이친수의 개수 + n-2자리 이친수의 개수
dp = [0 for _ in range(n+1)]
dp[1] = 1 

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])