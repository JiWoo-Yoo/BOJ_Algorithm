import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# index는 2부터 n까지만 취급할것임
erased = [False for _ in range(n+1)]
erased[0], erased[1] = True, True
erase_cnt = 0
p = 2
start_index = p
checked_p = True

# erase_order는 2부터 n까지 지워짐 여부를 담음
# erase_cnt는 몇 번째로 지워지는지 계산함

answer = p
# 알고리즘
# 1. erased에 False가 있으면(아직 모든 수를 지우지x)
while False in erased:
    # 2. 지우지 않은 수 중 가장 작은 수 p
    p = start_index
    checked_p = False
    for i in range(p, n+1):
        if i % p == 0:
            if not erased[i]:
                erased[i] = True
                erase_cnt += 1
                # print(i, end=' ')
                if erase_cnt == k:
                    answer = i
                    break
        else:
            if not checked_p:
                start_index = i
                checked_p = True
    if erase_cnt == k:
        answer = i
        break
# print(erased)
print(answer)
