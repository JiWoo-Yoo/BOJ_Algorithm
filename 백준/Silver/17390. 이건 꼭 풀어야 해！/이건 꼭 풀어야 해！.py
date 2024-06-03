# 완탐: 시간초과
# 답은 누적합
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a)
s = [0] + b[:]
for i in range(1, n+1):
    s[i] = s[i-1] + b[i - 1]
for i in range(q):
    l, r = map(int, input().split())
    if l > 1:
        print(s[r] - s[l-1])
    else:
        print(s[r])