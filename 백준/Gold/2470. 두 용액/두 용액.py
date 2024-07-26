# 합이 0에 가까운 두 용액 찾기 -> 절댓값이 작아야함
import sys
n = int(input())
liquids = list(map(int, input().split()))

# 오름차순 정렬
liquids.sort()

# 투 포인터
answer = []
left, right = 0, n-1
near_zero = 2000000000
while left < right:
    temp = liquids[left] + liquids[right]
    if near_zero > abs(temp):
        near_zero = abs(temp)
        answer = [liquids[left], liquids[right]]
        
        if temp == 0:
            break
    
    if temp < 0:
        left += 1 
    else:
        right -= 1 
        
print(' '.join(map(str, answer)))