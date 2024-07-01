n = int(input())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

# 모든 정점의 다른 정점까지의 최단경로 : 플로이드 워셜(O(n^3))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k] and g[k][j]:
                g[i][j] = 1

for r in g:
    for c in r:
        print(c, end=' ')
    print()