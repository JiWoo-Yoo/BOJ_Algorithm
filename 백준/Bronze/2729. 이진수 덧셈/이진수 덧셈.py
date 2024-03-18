def sum_bin(b1, b2):
    answer = ''
    up = False
    for i in range(len(b1)-1, -1, -1):
        if up: # 이전 연산에서 더한게 있으면
            if b1[i] == '0' and b2[i] == '0':
                answer += '1'
                up = False
            elif b1[i] == '1' and b2[i] == '1':
                answer += '1'
            else:
                answer += '0'
        else:
            if b1[i] == '0' and b2[i] == '0':
                answer += '0'
            elif b1[i] == '1' and b2[i] == '1':
                answer += '0'
                up = True
            else:
                answer += '1'
    if up: # 남아있으면
        answer += '1'
    return answer[::-1]  # 결과를 뒤집어 반환


def fill_zero(longer, shorter):
    shorter = shorter[::-1]  # shorter 문자열 뒤집기
    while len(shorter) < len(longer):
        shorter += '0'
    return shorter[::-1]  # 결과를 뒤집어 반환

t = int(input())
for _ in range(t):
    [b1, b2] = input().split()
    if len(b1) > len(b2):
        b2 = fill_zero(b1, b2)
    elif len(b2) > len(b1):
        b1 = fill_zero(b2, b1)
            
    print(int(sum_bin(b1, b2)))

