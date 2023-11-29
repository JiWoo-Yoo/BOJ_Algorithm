def fibonacci(n):
    fibs = [0 for i in range(n + 1)]
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, len(fibs)):
        fibs[i] = fibs[i - 2] + fibs[i - 1]
    return fibs[n]
            
def solution(n):
    answer = fibonacci(n)
    return answer % 1234567