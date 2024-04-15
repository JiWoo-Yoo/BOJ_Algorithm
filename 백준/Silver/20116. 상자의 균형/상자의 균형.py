# 누적합
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
cog = list(map(int, input().split()))
answer = 'stable'

for i in range(n - 1, 0, -1):
    if cog[i-1] - l < cog[i] / (n-i) < cog[i-1] + l:
        cog[i-1] = cog[i] + cog[i-1]
    else:
        answer = 'unstable'
        break
    
print(answer)
