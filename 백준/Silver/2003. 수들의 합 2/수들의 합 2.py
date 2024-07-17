n, m = map(int, input().split())
a = list(map(int, input().split()))

# 누적합
dp = [0 for _ in range(n)]
dp[0] = a[0]
for i in range(1, n):
	dp[i] = dp[i-1] + a[i]
	
cnt = 0
# j를 늘려가면서(O(n)) 합이 M이되는 i 찾기(O(n))
for j in range(n):
	for i in range(j+1):
		if dp[j] - dp[i] + a[i] == m:
			cnt += 1

print(cnt)