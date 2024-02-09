def GCM(a, b): # 최대공약수 : 유클리드 호제법
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def LCM(a, b): # 최소공배수 : a * b / 최대공약수
    return (a * b) // GCM(a, b)
    
    
n1, n2 = map(int, input().split())
print(GCM(n1, n2))
print(LCM(n1, n2))
