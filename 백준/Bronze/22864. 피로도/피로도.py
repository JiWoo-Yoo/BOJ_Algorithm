a, b, c, m = map(int, input().split())
tired = 0
total = 0

for t in range(1, 25):  # 하루는 1시간씩 24시간
    if tired + a <= m:  # 피로도가 한계 미만일 때 작업
        tired += a
        total += b
    else:  # 피로도가 한계를 넘으면 휴식
        tired = max(0, tired - c)  # 피로도는 음수가 될 수 없음

print(total)
