# 사탕 포장에 최소한으로 사용하는 상자의 수
# 그리디 알고리즘
t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    # 상자별 넓이 저장(r*c)할 배열
    box_s = []
    for i in range(n):
        r, c = map(int, input().split())
        box_s.append(r*c)
    # 넓이가 최대가 되는 상자부터 선택
    box_s.sort(reverse=True)
    sum_s = 0
    answer = 0
    for s in box_s:
        sum_s += s
        answer += 1
        if sum_s >= j: # 상자의 넓이 합이 사탕수 감당가능
            break
    print(answer)
