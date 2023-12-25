def solution(distance, rocks, n):
    rocks.sort()
    max_min = 0
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        removed = 0
        prev = 0
        
        for rock in rocks:
            if rock - prev < mid:
                # 돌을 제거하는 경우
                removed += 1
            else:
                # 돌을 제거하지 않는 경우
                prev = rock
        
        if distance - prev < mid:
            # 마지막 돌까지 제거하는 경우
            removed += 1
        
        if removed <= n:
            # 제거한 돌의 수가 n 이하인 경우
            max_min = max(max_min, mid)
            left = mid + 1
        else:
            # 제거한 돌의 수가 n 초과인 경우
            right = mid - 1
            
    return max_min
