# mCk * n-mCm-k / nCm
# m개에서 k개 선택 * 나머지 수 중 k제외선택 / 전체선택 수
# 위는 m개에서 k개를 고르고 그 나머지에서 m-k개를 고르는 확률.
# 따라서 k, k+1, k+2, ..., m 개를 선택하는 확률을 모두 더해야 함.

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total
    
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

n, m, k = map(int, input().split())
pos = 0
wp = combination(n, m)
while k <= m:
    if n-m < m-k:
        k += 1
        continue
    pos += combination(m, k) * combination(n-m, m-k) / wp
    k += 1
    
print(pos)
