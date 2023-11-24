def possible(answer):
    for x, y, a in answer:
        if a == 0: # 기둥이다!
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif a == 1: # 보다!
            if [x, y-1, 0] in answer or [x + 1, y-1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for order in build_frame:
        [x, y, a, b] = order
        if b == 0: # 제거하라!
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        elif b == 1: # 건축하라!
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
    return sorted(answer)