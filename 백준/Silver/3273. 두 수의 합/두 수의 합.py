# 수열 중 두 수의 합이 x가 되게끔 하는 두 수의
# 순서쌍 갯수 구하기
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
answer = 0

arr.sort()

l, r = 0, n - 1

while l < r:
    sum_lr = arr[l] + arr[r]
    if sum_lr == x:
        answer += 1
        l += 1
        r -= 1
    elif sum_lr > x:
        r -= 1
    elif sum_lr < x:
        l += 1

print(answer)
