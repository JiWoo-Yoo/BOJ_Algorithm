n = int(input())
answer = 0
while n > 0:
    if n % 5 == 0: # 5의 배수면
        answer += n // 5
        n = 0
        break
    else: # 5의 배수가 아니면 2씩 깎음
        n = n - 2
        answer += 1
if n != 0:
    answer = -1
print(answer)

