# 3개를 살 경우 가장 싼건 무료.
# n개의 유제품을 모두 살 때 필요한 최소비용.
# 아이디어: 가능한 3묶음으로 사고, 각 묶음의 최소가 최대한 커야함
# => 내림차순 정렬하여 앞에서부터 3의 배수씩 제거.

n = int(input())
dp = []# dairy products(o). dynamic programming(x).
for _ in range(n):
    dp.append(int(input()))

# 내림차순 정렬
dp.sort(reverse=True)

answer = 0

# 3묶음씩 묶고 그중 최소인 값 제거
for i in range(0, n, 3):
    answer += sum(dp[i:i+2])
    
print(answer)