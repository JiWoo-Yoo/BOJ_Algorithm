n, m = map(int, input().split())
# nCr = n!/(n-r)!r!

def factorial(n):
    facto = [1] * (n+1)
    if n > 1:
        for i in range(2, n+1):
            facto[i] = facto[i-1] * i
    return facto[n]

def combination(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))
    
print(combination(n, m))