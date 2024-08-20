# 1이면 단절점인지, 2이면 단절선인지 대답
import sys
input = sys.stdin.readline

# 트리 정점의 개수
n = int(input())
edges = []
adj = [[] for i in range(n+1)]

# 간선 정보
for _ in range(n-1):
    edge = list(map(int, input().split()))
    edges.append(edge)
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])


# 질의 개수
q = int(input())
answer = ''
for i in range(q):
    t, k = map(int, input().split())
    if t == 1: # 단절점 여부 검사
        # 연결된 간선이 2개 이상이면 단절점.
        if len(adj[k]) >= 2:
            answer = 'yes'
        else:
            answer = 'no'
    
    elif t == 2: # 단절선 여부 검사
        # 사이클이 존재하지 않기에 모든 선이 단절선.
        answer = 'yes'
    print(answer)