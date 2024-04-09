import sys
input = sys.stdin.readline

n = int(input())
difficulty = list(map(int, input().split()))
q = int(input())

# i악보가 i+1 악보보다 어려우면 실수함
# 마지막 y악보에서는 실수 안함
# 오늘 피아노 체조에서 실수하는 곡 고르기

# 누적합 구해두기(i까지의 구간에서 실수하는 수)
is_hard = [0 for i in range(n+1)]
for i in range(1, n):
    if difficulty[i-1] > difficulty[i]:
        is_hard[i] = is_hard[i-1] + 1
    else:
        is_hard[i] = is_hard[i-1]

for _ in range(q):
    x, y = map(int, input().split())
    answer = is_hard[y - 1] - is_hard[x - 1]
    print(answer)
    
