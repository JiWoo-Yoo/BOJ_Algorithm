# 성의 첫 글자가 같은 선수 5명 선발(5명미만-기권)
# 가능한 성의 첫 글자 사전순으로 출력(없으면 PREDAJA)
# 아이디어: 첫글자별로 cnt-> 5 이상인 경우 정렬해서 출력

n = int(input())
surren = "PREDAJA"
player = {}
for i in range(n):
    f_c = input()[0]
    if f_c in player:
        player[f_c] += 1
    else:
        player[f_c] = 1

answer = ''

for key in player:
    if player[key] >= 5:
        answer += key

if answer == '':
    print(surren)
else:
    print(''.join(sorted(answer)))