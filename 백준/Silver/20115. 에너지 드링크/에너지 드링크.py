n = int(input())
drink = list(map(int, input().split()))

# 정렬
drink.sort()

answer = 0
for i in range(n - 1):
    drink[n - 1] += drink[i] * 0.5
print(drink[n-1])