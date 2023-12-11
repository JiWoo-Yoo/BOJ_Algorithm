def find_parent(parent, x): # 특정 원소가 속한 집합을 찾기
    if parent[x] != x: # 루트 노드를 찾을 때까지 재귀 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합을 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    answer = 0
    # 크루스칼 알고리즘
    parent = [0] * (n + 1) # 부모 테이블 초기화
    for i in range(1, n + 1): # 부모를 자기 자신으로 초기화
        parent[i] = i
    
    sorted_edges = sorted(costs, key=lambda x:x[2]) # 간선을 비용 오름차순으로 정렬
    
    for edge in sorted_edges: # 간선을 하나씩 확인
        a, b, cost = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함(union-find)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
            
    return answer