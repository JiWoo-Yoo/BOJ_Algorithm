# 유성과 땅의 충돌 모양 구현
# 주의: 떨어졌을 시 유성은 모양을 유지한다.
r, s = map(int, input().split())
before_photo = []
for i in range(r):
    before_photo.append(input())
        

after_photo = []
# 열을 돌며 유성과 땅이 가장 가까운 부분 찾은 후 최솟값만큼 유성 낙하
def min_dist():
    dist = r
    for i in range(s):
        meteor = -r # 유성이 없을 경우
        for j in range(r):
            if before_photo[j][i] == 'X':
                meteor = j # 유성의 행 저장
            elif before_photo[j][i] == '#':
                dist = min(j - meteor - 1, dist) # 유성과 땅의 거리 저장
                break
    return dist

min_d = min_dist()

# 유성 낙하
# 내려간 만큼 공기로 채우기
for i in range(min_d):
    temp = []
    for j in range(s):
        if before_photo[i][j] == "#":
            temp.append("#")
        else:
            temp.append(".")
    after_photo.append(temp)

# min_d만큼 이동한 유성 위치 표시
for i in range(min_d, r):
    temp = []
    for j in range(s):
        if before_photo[i-min_d][j] == "X":
            temp.append("X")
        elif before_photo[i][j] == "#":
            temp.append("#")
        else:
            temp.append(".")
    after_photo.append(temp)
    
for i in range(r):
    for j in range(s):
        print(after_photo[i][j], end='')
    print()
