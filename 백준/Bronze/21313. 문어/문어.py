# 길이 n의 문어 손수열 중 사전순으로 가장 앞서는 것
# 문어는 같은 번호의 숫자 손만 잡을 수 있음(1번~8번)
# 그리디 & 애드혹(일반화될 수 없는 해답)
n = int(input())
suwolae = [0 for _ in range(n)]
suwolae[0] = 1

for i in range(1, n):
    if suwolae[i-1] == 1:
        suwolae[i] = 2
    elif i == n-1:
        if n % 2 == 0:
            suwolae[i] = 2
        else:
            suwolae[i] = 3
    else:
        suwolae[i] = 1

for hand in suwolae:
    print(hand, end=' ')