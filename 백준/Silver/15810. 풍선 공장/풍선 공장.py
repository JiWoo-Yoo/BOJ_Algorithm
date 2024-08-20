n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 1, max(arr)*m
answer = right

while left <= right:
    mid = (left + right) // 2
    
    # mid시간동안 m개 풍선을 불 수 있는가?
    bal_cnt = 0
    for staff in arr:
        bal_cnt += mid // staff
    
    if bal_cnt >= m: # 불 수 있으면
        right = mid - 1
        answer = mid
        
    else: # 시간이 부족하면
        left = mid + 1
        
print(answer)