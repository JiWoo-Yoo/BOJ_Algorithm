# 가장 많은 수익을 올린 구간의 수익 출력
while True:
    n = int(input())
    if n == 0:
        break
    else:
        dp = [0] * (n+1)
        for i in range(1, n + 1):
            p = int(input())
            dp[i] = max(dp[i-1] + p, p)
        print(max(dp[1:]))