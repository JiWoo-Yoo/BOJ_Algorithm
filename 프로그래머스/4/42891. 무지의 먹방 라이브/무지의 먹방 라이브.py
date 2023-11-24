import heapq
def solution(food_times, k):
    if sum(food_times) <= k: # 다 먹은 후에 고장남.
        return -1
    else:
        # 우선순위 큐를 사용하여 가장 시간이 적게 걸리는 음식부터 해치운다.(그리디)
        q = []
        length = len(food_times) # 음식 수
        for i in range(length): # 우선순위 큐(최소힙)에 집어넣기
            heapq.heappush(q, (food_times[i], i + 1))
        sum_value = 0 # 먹는데 걸린 시간
        previous = 0 # 직전에 다 먹은 음식의 시간

        while sum_value + ((q[0][0] - previous) * length) <= k:
            now = heapq.heappop(q)[0]
            sum_value += (now - previous) * length
            length -= 1
            previous = now
            
        result = sorted(q, key = lambda x:x[1])
        return result[(k - sum_value) % length][1]
    