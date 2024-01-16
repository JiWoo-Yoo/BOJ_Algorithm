# 플로이드 워셜 
n = int(input())
m = int(input())
INF = int(1e9)
cost = [[INF for i in range(n+1)] for j in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(c, cost[a][b])
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost[a][b] = min(cost[a][b], cost[a][k] + cost[k][b])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == INF or i == j:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()
