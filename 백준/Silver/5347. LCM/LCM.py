# 최대공약수: 유클리드 호제법
# 최소공배수: a * b / 최대공약수

def GCD(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def LCM(a, b):
    return a * b // GCD(a, b)


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))
