# n개의 파티장을 가진 놀이동산
# 연결된 도로는 일방통행

# 한 파티장에서 다른 파티장까지 시간내에 도착할 수 있는지 알아보기
can = 'Enjoy other party'
cannot = 'Stay here'

# 그래프 - 플로이드 워셜
# a에서 b까지 가는 최단거리 구하기, 최단거리를 c와 비교

n, m = map(int, input().split())

# time[i][j] => i에서 j까지의 이동시간
time = [] 
for i in range(n):
    time.append(list(map(int, input().split())))
    
# k를 거쳐가는 i->j와 그냥 i->j 중 최솟값을 갱신
for k in range(n):
    for i in range(n):
        for j in range(n):    
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])


# a: 현재 위치한 파티장
# b: 다음 파티가 열리는 파티장
# c: 지금으로부터 다음 파티가 열리는데 걸리는 시간 c
for i in range(1, m+1):
    a, b, c = map(int, input().split())
    
    # 손님이 시간내에 b에 도착할 수 있는지
    if time[a-1][b-1] <= c:
        print(can)
    else:
        print(cannot)