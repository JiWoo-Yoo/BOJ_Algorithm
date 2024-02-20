# 3합 0이 되는 경우의 수
import bisect
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))
# [추가됨] --> rstrip 까지 쓰는게 입력이 더 빠르다
answer = 0

# 정렬을 한다.
a.sort()

cache = set(a)
# [추가됨] --> 어차피 c가 a 안에 존재하지 않는 경우 이분탐색을 진행할 필요 없음

# 두 값을 먼저 찾는다.
for i in range(0, n-2):
    for j in range(i+1, n-1):
        # a + b = - c가 되는 c를 찾아야 함
        c = -(a[i] + a[j])
        if c in cache:
            upper = bisect.bisect_right(a, c, lo=j+1)
            lower = bisect.bisect_left(a, c, lo=j+1)
            answer += (upper - lower)

print(answer)