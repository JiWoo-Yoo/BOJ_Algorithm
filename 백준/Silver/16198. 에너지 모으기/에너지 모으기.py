# 백트래킹?
def collectE(marbles):
    max_sum = 0
    if len(marbles) == 2: # x 선택 불가
        return 0
    for i in range(1, len(marbles) - 1):
        collect = marbles[i-1]*marbles[i+1]
        # 구슬 x 제거
        new_marbles = marbles[:i] + marbles[i+1:]
        curr_sum = collect + collectE(new_marbles)
        max_sum = max(curr_sum, max_sum)
    return max_sum


n = int(input())
mw = list(map(int, input().split()))
print(collectE(mw))
