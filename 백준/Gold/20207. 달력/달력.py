n = int(input())
plans = [0 for j in range(1001)]
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        plans[i] += 1

answer = 0
max_h = 0
s_i = 0
started = False
# 일별로 확인하면서 최대 세로 길이 계산
for i in range(len(plans)):
    if not started: # 일정 안세는중
        if plans[i] != 0: # 일정 발견
            started = True
            s_i = i
    if started: # 일정 세는중
        if plans[i] == 0: # 일정 없음
            started = False
            answer += max_h * (i - 1 - s_i + 1)
            max_h = 0
        else: # 일정 있음
            max_h = max(max_h, plans[i])
if started:
    started = False
    answer += max_h * (n - 1 - s_i + 1)
print(answer)
