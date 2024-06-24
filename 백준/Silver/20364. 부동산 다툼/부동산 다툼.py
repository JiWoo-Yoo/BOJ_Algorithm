import sys
input = sys.stdin.readline
n, q = map(int, input().split())

# 점유된 땅을 추적하기 위한 집합
occupied = set()

# i번째 오리가 원하는 땅 번호
duck_ground = [int(input()) for _ in range(q)]

for ground in duck_ground:
    current = ground
    conflict = 0
    # 원하는 땅을 루트(1)까지 추적
    while current > 0:
        if current in occupied:
            conflict = current
        current //= 2
    if conflict == 0:
        occupied.add(ground)
    print(conflict)
