n, m = map(int, input().split())
h = list(map(int, input().split()))
side_ks = [0 for i in range(n)]
for i in range(m):
	a, b, k = map(int, input().split())
	side_ks[a-1] += k
	if b < n:
	    side_ks[b] -= k

dp = [0 for i in range(n)]
dp[0] = side_ks[0]
for i in range(1, n):
	dp[i] = dp[i-1] + side_ks[i]

result = []
for i in range(n):
	result.append(h[i] + dp[i])

for i in range(n):
	print(result[i], end=' ')