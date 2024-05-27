# 현우가 N일동안 M번 통장에서 돈을 K원씩 빼서 씀.
# 수중의 돈이 부족하면 입금하고 K원 뺌.
# 수중의 돈이 충분하면 그대로 씀.
# 최소 K 구하는 프로그램
n, m = map(int, input().split())
money = []

for i in range(n):
    money.append(int(input()))
    
# 이분 탐색: mid로 k의 값을 구함
start = min(money)
end = sum(money)
k = 1

while start <= end:
    mid = (start + end) // 2
    wd_cnt = 1
    balance = mid
    for use in money:
        # 돈이 모자르면 인출
        if balance < use:
            wd_cnt += 1
            balance = mid
        # 지불
        balance -= use
    if wd_cnt > m or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1
        k = mid
        
print(k)