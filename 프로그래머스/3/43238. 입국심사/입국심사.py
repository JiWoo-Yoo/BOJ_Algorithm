def solution(n, times):
    answer = 0
    times.sort() # 이분탐색을 하려면 정렬해야함
    mini = times[0] # 왼쪽 범위: 심사관중 가장 적게드는 심사관에 1명이 심사받음.
    maxi = times[-1] * n # 오른쪽 범위: 가장많이걸리는심사관에 n명다 심사받음.
    while mini <= maxi:
        mid = ( mini + maxi ) // 2
        people = 0 # 주어진 시간 mid 안에 심사할 수 있는 사람 수
        
        for time in times:
            people += mid // time # 적게 걸리는 심사관부터 심사가능한 사람수만큼 심사
        
            if people >= n: # n명 다 심사 받으면 
                break
        
        if people >= n: # 시간이 충분하군.
            answer = mid
            maxi = mid - 1
        elif people < n: # 시간이 부족하군.
            mini = mid + 1
    return answer