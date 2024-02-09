# 회의실에 대해 N개의 회의를 겹치지 않고 진행
# 사용하는 회의의 최대 개수 구하기
n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))

# 끝나는 시간으로 배열 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 첫번째 회의 끝나는 시간 <= 두번째 회의 시작
answer = 0
end1 = 0

for start2, end2 in meetings:
    if end1 <= start2:
        answer += 1
        end1 = end2

print(answer)
