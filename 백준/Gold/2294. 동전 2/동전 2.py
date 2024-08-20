# DP. n종류의 동전으로 k합을 만들 때 최소 동전의 개수
n, k = map(int, input().split())
# DP를 k의 최대보다 크게 초기화(dp[i] == 합이 i가 되는 동전의 최소 개수)
dp = [10001] * (k+1)
dp[0] = 0

coins = []
# 동전 종류 입력받기
for _ in range(n):
    coins.append(int(input()))

# 동전 종류별로 오름차순 정렬
coins.sort()

# 각 동전을 사용해 dp 갱신
for coin in coins:
    for i in range(coin, k+1): # coin으로 coin보다 작은값을 만들수없음
        dp[i] = min(dp[i], dp[i-coin] + 1)

answer = -1 if dp[k] == 10001 else dp[k]
print(answer)