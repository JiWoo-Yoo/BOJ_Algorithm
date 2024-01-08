def check_switch():
    n, m = map(int, input().split())
    switch_list = []

    for i in range(n):
        temp = list(map(int, input().split()))
        switch_list.append(temp[1:])

    lamp_list = [0 for i in range(m + 1)]

    for s in switch_list: # 각 스위치의
        for l in s: # 켤 수 있는 램프를
            lamp_list[l] += 1 # 켠다

    for s in switch_list: # 한 스위치를 꺼도 켜지면 1
        for l in s:
            lamp_list[l] -= 1
        if 0 not in lamp_list[1:]: # 꺼진 스위치가 없음
            return 1
        for l in s:
            lamp_list[l] += 1 # 원상복귀
    return 0
        
print(check_switch())
