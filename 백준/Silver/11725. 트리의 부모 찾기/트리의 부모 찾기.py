import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한을 늘림

n = int(input())
adj_list = [[] for _ in range(n+1)]

# 입력 받아서 인접 리스트 구성
for _ in range(n-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 모든 노드의 부모 리스트 생성
parents = [0] * (n + 1)
visited = [False] * (n + 1)

# DFS를 통해 각 노드의 부모 설정 (반복적 방식으로 변경)
stack = [(1, 0)]  # (현재 노드, 부모 노드)

while stack:
    node, parent = stack.pop()
    parents[node] = parent
    visited[node] = True
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            stack.append((neighbor, node))

# 각 노드의 부모 정보 출력 (노드 1은 부모가 없으므로 제외)
for i in range(2, n+1):
    print(parents[i])
