# 대칭 차집합 = (A-B) U (B-A)
import sys
input = sys.stdin.readline
na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

def sds(a, b, na, nb):
    # 완전탐색으로 풀기 - set 이용
    # 1. A - B
    first_operand = list(filter(lambda x : x not in b, a))
    
    # 2. B - A 
    second_operand = list(filter(lambda x : x not in a, b))
    
    return first_operand + second_operand
    
print(len(sds(a, b, na, nb)))