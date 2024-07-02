# 주어진 수열에서 주어진 구간의 합 구하기
# 시간초과 방지: 누적합
n = int(input())
a = list(map(int, input().split()))
m = int(input())
dp = [0 for i in range(n+1)]

# 누적합 구하기 
for i in range(1, n + 1):
    dp[i] = dp[i-1] + a[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
