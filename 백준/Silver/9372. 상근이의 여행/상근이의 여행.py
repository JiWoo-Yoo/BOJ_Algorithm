# 상근이의 N개국 여행 - 타야 하는 비행기의 최소 개수 출력
# 무방향 그래프
# 아이디어: 신장 트리 이용(모든정점연결, 사이클x, n-1개의 간선)

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    for j in range(m):
        a, b = map(int, input().split())
    print(n-1)
    