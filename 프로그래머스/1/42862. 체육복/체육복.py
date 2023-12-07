def check_poor(index, people):
    if  people[index] > 1 and people[index - 1] == 0:
        people[index] -= 1
        people[index - 1] += 1
    if index < len(people) - 1:
        if people[index] > 1 and people[index + 1] == 0:
            people[index + 1] += 1
            people[index] -= 1
def solution(n, lost, reserve):
    answer = 0
    cnt_cloth = [1 for _ in range(n + 1)]
    for student in reserve:
        cnt_cloth[student] += 1
    for student in lost:
        cnt_cloth[student] -= 1
    
    cnt_cloth[0] = 10
    for i in range(1, n + 1):
        check_poor(i, cnt_cloth)
    for cnt in cnt_cloth[1:]:
        if cnt > 0:
            answer += 1
    return answer