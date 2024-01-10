# m개에서 n개를 선택하는 경우의 수 구하기
t = int(input())

def factorial(n):
    # 팩토리얼 구하기
    sol = 1
    for i in range(1, n + 1):
        sol *= i
    return sol

def combination(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

for _ in range(t):
    nn, m = map(int, input().split())
    print(combination(m, nn))
