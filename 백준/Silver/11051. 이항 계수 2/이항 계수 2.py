n, k = map(int, input().split())

def factorial(num):
    if num <= 1:
        return 1
    return factorial(num-1) * num
    
    
answer = factorial(n) // (factorial(n-k) * factorial(k))

print(answer % 10007)