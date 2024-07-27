# v마을, e도로(일방통행). 마을 (1~v)
# 도로의 길이의 합이 가장 작은 사이클 찾기
import sys
v, e = map(int, input().split())
graph = [[sys.maxsize]*(v+1) for j in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c  #방향그래프
# pypy3이기에 O(n^3)
# 플루이드 워셜 알고리즘에서 자기자신으로 가는 경로 포함

for k in range(1, v+1):
   for i in range(1, v+1):
      for j in range(1, v+1):
         graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
# 경로 찾는 것이 불가능할 경우 -1 출력
answer = sys.maxsize
for i in range(1, v+1):
   answer = min(graph[i][i], answer)
   
if answer == sys.maxsize:
   print(-1)
else:
   print(answer)