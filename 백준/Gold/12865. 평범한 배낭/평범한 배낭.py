# n개의 물건은 각각 무게W와 가치V를 가짐 
# 최대 k만큼의 무게 들기 가능 
# 최대로 즐기기(V) 위해 배낭에 넣을 수 있는 물건 가치의 최댓값 구하기 
# 배낭 문제

n, k = map(int, input().split())
w = [0 for i in range(n+1)]
v = [0 for i in range(n+1)]
for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())

dp = [[0 for i in range(k+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # 현재 물건을 넣을 수 없는 경우
        if j - w[i] < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])

print(dp[n][k])