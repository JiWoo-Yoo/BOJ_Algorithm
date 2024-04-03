import sys
input = sys.stdin.readline
n = int(input())

# 소수 입력을 받아 리스트에 저장
dp = [float(input()) for _ in range(n)]

# 자신까지 곱한것과 자신을 비교
# 더 큰 것을 저장
for i in range(1, n):
    dp[i] = max(dp[i], dp[i]*dp[i-1])

# print(round(max(dp), 3)) # 1.0
print('%0.3f' % max(dp)) # 1.000
