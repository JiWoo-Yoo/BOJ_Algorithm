# 문자열을 최대한 완전히 복원(h만큼 세로로, w만큼 가로로 번짐)
n, h, w = map(int, input().split())
strings = []
for _ in range(h):
    strings.append(input())

answer = ''

# 주어진 index에서 가로로 w, 세로로 h만큼 탐색하면서 '?'가 아닌 문자가 있으면 반환
def find_c(x, h, w, strings):
    for i in range(h):
        for j in range(x, x + w):
            if strings[i][j] != '?':
                return strings[i][j]
    return '?'

# x축으로 가로(w)로 번진만큼 건너뛰며 find_c 실행
for x in range(0, len(strings[0]), w):
    answer += find_c(x, h, w, strings)

print(answer)