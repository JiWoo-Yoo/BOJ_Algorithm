# 한 줄씩 받아서
while True:
    line = input()
    if line == 'END': # 끝이면
        break
    # 뒤집은 결과를 출력
    print(line[::-1])

