# 수열에서 두 수를 골랐을 때
# 차이가 M 이상이면서 (차이가)제일 작은 경우

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

# 2. 투 포인터
a.sort()

min_num = int(1e12)
l, r = 0, 0
while l < n and r < n:
    diff = a[r] - a[l]
    if diff >= m:
        min_num = min(min_num, diff)
        l += 1
    elif diff < m:
        r += 1
print(min_num)
