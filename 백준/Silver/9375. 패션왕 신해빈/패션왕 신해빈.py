# 의상의 모든 조합 구하기 ( 선글라스만 써도 알몸이 아님 )
t = int(input())
for _ in range(t):
    combination = {}
    n = int(input())
    for i in range(n):
        cloth, ctype = map(str, input().split())
        if ctype in combination.keys():
            if cloth not in combination[ctype]:
                combination[ctype].append(cloth)
        else:
            combination[ctype] = [cloth]
        
    answer = 1
        
    for key in combination: # +1: '벗었다'
        answer *= (len(combination[key]) + 1)
    
    # 알몸을 뺌
    print(answer - 1)