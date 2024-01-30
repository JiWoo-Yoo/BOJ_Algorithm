def solution(sizes):
    answer = 0
    max_size = 0
    # 큰 값을 찾아서
    for size in sizes:
        max_size = max(max(size), max_size)
        
    max_min = 0
    # 작은 값을 찾아서
    for size in sizes:
        max_min = max(min(size), max_min)
    return max_size * max_min