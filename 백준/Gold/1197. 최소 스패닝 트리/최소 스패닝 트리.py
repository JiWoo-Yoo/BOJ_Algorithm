# 크루스칼 MST 알고리즘
# 참고: https://techblog-history-younghunjo1.tistory.com/262

# find 연산
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# union 연산
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
edges = []
total_cost = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
# 부모 테이블 초기화
parent = [0] * (v + 1)
for i in range(1, v+1):
    parent[i] = i
    
# 간선 기준 오름차순 정렬
edges.sort()

# 간선 하나씩 확인
for i in range(e):
    c, a, b = edges[i]
    # 사이클 확인: 부모노드 같으면 사이클
    if find(parent, a) != find(parent, b):
        # 사이클 없으면 MST에 포함
        union(parent, a, b)
        total_cost += c
        
print(total_cost)
