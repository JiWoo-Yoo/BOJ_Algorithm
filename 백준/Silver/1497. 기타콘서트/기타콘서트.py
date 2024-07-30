import itertools

n, m = map(int, input().split())
guitars_bit = []
# 'Y' -> 1, 'N' -> 0
for _ in range(n):
    guitar = list(map(str, input().split()))
    temp = []
    for ch in guitar[1]:
        if ch == 'Y':
            temp.append(1)
        else:
            temp.append(0)
    guitars_bit.append(temp)

nCr = []
for i in range(n + 1):  # nCr[i]는 n개 중에 i개를 선택하는 조합들
    nCr.append([])
    combinations = itertools.combinations(guitars_bit, i)
    for comb in combinations:
        nCr[i].append(list(comb))
# print(nCr)

# 기타 개수별 가능 최대 노래 수
max_per_guitars = [0]
for i in range(1, n+1): # i개를 선택하는 조합 묶음 순회 (예. 2개를 선택한 조합들)
    max_comb = 0
    for comb in nCr[i]: # 각 조합묶음의 조합 순회 (예. 2개를 선택한 조합 1)
        songs = [0] * m # 조합을 or연산하여 해당 기타 조합으로 가능한 곡 수 나타냄
        for guitar in comb:
            for j in range(m):
                songs[j] = guitar[j] or songs[j]
        max_comb = max(songs.count(1), max_comb)
        # print(songs, max_comb)
    max_per_guitars.append(max_comb)
    
# 최대 송을 가진 가장 작은 인덱스(기타수) 반환
answer = -1
max_song = max(max_per_guitars)
if max_song == 0:
    answer = -1
else:
    for i in range(n+1):
        if max_per_guitars[i] == max_song:
            answer = i
            break
print(answer)