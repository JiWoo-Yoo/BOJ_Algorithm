# 소수들의 최소공배수 구하기
import math

def boj_21919():
    n = int(input())
    a = list(map(int, input().split()))
    
    #1. 소수 구하기
    prime_nums = []
    def is_prime_num(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
        
    for num in a:
        if is_prime_num(num):
            prime_nums.append(num)
    
    #2. 최소 공배수 구하기
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
        
    def lcm(a, b):
        return a * b // gcd(a, b)
        
    if len(prime_nums) == 0:
        return -1
    lcm_n = prime_nums[0]
    for i in range(1, len(prime_nums)):
        lcm_n = lcm(lcm_n, prime_nums[i])
    return lcm_n

print(boj_21919())
