def solution(n, results):
    INF = int(1e9)
    # 승패기록 2차원배열 값을 모두 무한대로 초기화
    record = [[INF for _ in range(n+1)] for i in range(n+1)]
    # 자기 자신으로 가는 부분은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                record[a][b] = 0
                
    # 각 승패에 관한 정보로 초기화
    for winner, loser in results:
        record[winner][loser] = 1
        record[loser][winner] = 0
    
    # 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1): # k를 거쳐가는 경우
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if record[a][k] == 1 and record[k][b] == 1:
                    record[a][b] = 1
                    record[b][a] = 0
                
    # 자기 자신과의 결과를 제외한 승패 결과가 전부 있는 경우 count
    cnt = 0
    for i in range(1, n + 1):
        # print(record[i][1:])
        if INF not in record[i][1:]:
            cnt += 1
    return cnt