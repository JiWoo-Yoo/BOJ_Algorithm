def solution(arr):
    
    mins, maxs = 0, 0
    summation = 0
    for i in range(len(arr)-1, -1, -1) :
        if arr[i] == '+' :
            continue
        elif arr[i] == '-' :
            tmpmin, tmpmax = mins, maxs
            mins = min(-(summation + tmpmin), -summation + tmpmin)
            num = int(arr[i+1])
            maxs = max(-(summation + tmpmin), -num+(summation - num)+tmpmax )
            summation = 0
        else :
            summation += int(arr[i])
    maxs += summation
    return maxs