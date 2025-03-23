def solution(survey, choices):
    answer = ''
    # 알고리즘 유형: 순회 or 배열(로 추정)
    # 시간복잡도: 
    # 1. 유형별로 count하는 객체 & 지표별 유형 arr작성
    typeCnt = {'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0}
        
    indicator = [['R', 'T'],
                ['C', 'F'],
                ['J', 'M'],
                ['A', 'N']]
    
    # 미리 사전순 정렬
    for i in indicator:
        i.sort()
    
    # 2. survey를  순회하며 choices에 맞춰 typeCnt에 저장
    idx = 0
    for idx, question in enumerate(survey):
        no_agr_q, agr_q = question[0], question[1]
        
        score = choices[idx] - 4  # 4를 기준으로 가중치 계산 (-3 ~ 3)
        
        if score < 0:  # 비동의
            typeCnt[no_agr_q] += abs(score)
        elif score > 0:  # 동의
            typeCnt[agr_q] += score
        
    # 3. 지표별로 많이나온 유형 선택하여 answer 추출
    for i in range(4):
        indicator_types = indicator[i]
        
        if typeCnt[indicator_types[0]] >= typeCnt[indicator_types[1]]:
            answer += indicator_types[0]
        else:
            answer += indicator_types[1]
        
    return answer