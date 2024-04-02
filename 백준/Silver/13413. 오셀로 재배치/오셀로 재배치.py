# 연산: 두 말의 위치 바꾸기, 말을 뒤집어 색상 변경
# 최소 연산 횟수 구하기
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    init = input()
    tobe = input()
    
    cnt_swap = 0
    cnt_flip = 0
    
    # 1. 두 말의 위치 바꾸기
    diff_w_cnt = 0
    diff_b_cnt = 0
    for i in range(n):
        if init[i] != tobe[i]:
            if init[i] == 'W':
                diff_w_cnt += 1
            elif init[i] == 'B':
                diff_b_cnt += 1
    # 1번 연산으로 같게 만들 수 없으면
    if diff_w_cnt != diff_b_cnt:
        cnt_swap = max(diff_w_cnt, diff_b_cnt)
    # 1번 연산으로 같게 만들 수 있으면
    else:
        cnt_swap = diff_w_cnt
        
    # 2. 말을 뒤집어 색상 변경
    for i in range(n):
        if init[i] != tobe[i]:
            cnt_flip += 1
            
    print(min(cnt_swap, cnt_flip))
