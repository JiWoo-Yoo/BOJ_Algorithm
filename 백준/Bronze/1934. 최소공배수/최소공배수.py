# a와 b의 최소공배수 구하기
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
        
def lcm(a, b):
    return a * b // gcd(a, b)
    
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(max(a, b), min(a, b)))
        

