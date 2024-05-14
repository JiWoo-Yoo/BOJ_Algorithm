# 백준 블로그(21921, 실버3)
# x일동안 가장 많이 들어온 방문자 수와 기간을 출력하는 프로그램

import sys
input = sys.stdin.readline

n, x = map(int, input().split())

visitor = list(map(int, input().split()))

# 구해야 할 것: max값과, max값이 나타나는 구간
# 즉, 처음 한바퀴 max값을 구하고, 또한바퀴 돌며 max값이 나타나는 구간을 구해야함
# 즉, 구간별 합을 저장하는 누적합 배열이 필요함

sum_per_section = []

# max값 구하기: 슬라이딩 윈도우를 사용하여 시간 줄이기
window_sum = sum(visitor[:x])
sum_per_section.append(window_sum)
max_cnt = window_sum

for i in range(1, n - x + 1):
    window_sum = window_sum + visitor[i + x - 1] - visitor[i - 1]
    sum_per_section.append(window_sum)
    max_cnt = max(max_cnt, window_sum)
    
# max 구간 세기: 누적합 해놓은 곳을 하나하나 비교
cnt = 0
for section in sum_per_section:
    if section == max_cnt:
        cnt += 1
        
if max_cnt == 0:
    print('SAD')
else:
    print(max_cnt)
    print(cnt)