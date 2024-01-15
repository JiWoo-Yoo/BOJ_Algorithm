import heapq

def combine_min(n, chapters):
    heapq.heapify(chapters)
    total_cost = 0
    while len(chapters) > 1:
        min1 = heapq.heappop(chapters)
        min2 = heapq.heappop(chapters)
        temp = min1 + min2
        total_cost += temp
        heapq.heappush(chapters, temp)
    return total_cost

t = int(input())
for _ in range(t):
    n = int(input())
    chapters = list(map(int, input().split()))
    print(combine_min(n, chapters))
