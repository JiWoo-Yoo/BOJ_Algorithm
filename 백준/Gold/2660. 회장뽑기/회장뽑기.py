def pick_president():
    n = int(input())
    INF = 1e9
    pal = [[INF for i in range(n+1)] for j in range(n+1)]
    while True: # 친구 관계를 표시
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        pal[a][b] = 1
        pal[b][a] = 1
    
    for i in range(n + 1): # 자기 자신으로 가면 0
        pal[i][i] = 0
        
    # 플루이드 워셜 변형으로 친구의 친구의... 관계 표시
    for k in range(1, n + 1): # k를 거쳐가는 경우 비교
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                pal[a][b] = min(pal[a][b], pal[a][k] + pal[k][b])
                    
    # 회장후보의 점수, 후보 수, 회장후보 뽑기
    presidents = []
    score = INF
    for k in range(1, n + 1): # 점수 구하기
        if INF in pal[k][1:]: # 모르는 친구를 가진 녀석이면
            continue # 후보탈락
        else: # 모든애랑 아는 사이면
            temp = max(pal[k][1:]) # 친구의 친구의 ... 몇 까지 있는지
            score = min(score, temp) # 회장후보의 점수는 가장 작아야 함
    
    for k in range(1, n + 1): # 후보 뽑기
        if INF in pal[k][1:]: # 모르는 친구를 가진 녀석이면
            continue # 후보탈락
        else: # 모든애랑 아는 사이면
            if score == max(pal[k][1:]): # 회장후보 점수가 같으면 뽑기
                presidents.append(k)
            
    presidents = sorted(presidents)
    print(score, len(presidents))
    for p in presidents:
        print(p, end=' ')
            
     
pick_president()
