# 설탕 N킬로그램 배달 시 가져가야 하는 봉지 최소 개수 구하는 프로그램
# 봉지는 3킬로, 5킬로짜리 있음.
# 그리디

n = int(input())
answer = 0

while n >= 3:
    if n % 5 == 0:
        answer += n // 5
        n = n % 5
    else:
        n = n - 3
        answer += 1

if n > 0:
    answer = -1

print(answer)
    