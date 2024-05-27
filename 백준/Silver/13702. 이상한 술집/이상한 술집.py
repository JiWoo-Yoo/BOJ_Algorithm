# 막걸리 용량은 랜덤
# N개의 주전자를 갖고 자신포함 K명에게 막걸리 같은양 분배
# 분배 후 주전자에 막걸리 남으면 버림.
# K명에게 최대한 많은 양의 막걸리를 분배할 수 있는 용량 구하기

n, k = map(int, input().split())
kettle_vol = []
for i in range(n):
    kettle_vol.append(int(input()))
    
start = 1 
end = sum(kettle_vol)

answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    # mid값으로 몇 명을 줄 수 있는가
    for vol in kettle_vol:
        cnt += (vol // mid)
    if cnt >= k:
        answer = mid
        start = mid + 1 
    else:
        end = mid - 1
print(answer)