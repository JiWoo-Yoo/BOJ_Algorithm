n = int(input())

cnt = 0
num = 0

if n == 0:
    cnt = 1
else:
    while num != n:
        if cnt == 0:
            num = n
        str_num = str(num)
        if len(str_num) == 1:
            str_num = '0' + str_num
        # 1. 두 자리 더하기
        str_sum = int(str_num[0]) + int(str_num[1])
        # 2. 십의자리(이번 turn의 수의 일의자리), 일의자리(1에서 더한 값)
        num = int(str_num[1] + str(str_sum)[-1])
        cnt += 1
    
print(cnt)