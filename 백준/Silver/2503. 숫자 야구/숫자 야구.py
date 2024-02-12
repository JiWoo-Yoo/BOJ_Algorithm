from itertools import permutations

# 1. 가능한 세자리수 전부 구하기
num = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))
    
# 2. s, b에 따라 소거하기    
n = int(input())
del_i = []
for _ in range(n):
    data = input().split()
    ques, s, b = data[0], int(data[1]), int(data[2])
    for i in range(len(num)):
        strike, ball = 0, 0
        for c in range(3):
            if num[i][c] == ques[c]:
                strike += 1
            elif num[i][c] in ques:
                ball += 1
        if strike != s or ball != b:
            del_i.append(i)

answer = 0
for i in range(len(num)):
    if i not in del_i:
        answer += 1
        
print(answer)
