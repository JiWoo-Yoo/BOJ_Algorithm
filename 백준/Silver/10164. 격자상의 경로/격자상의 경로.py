import math
from math import factorial

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n, m, k = map(int, input().split())

if k == 0:
    answer = comb(n + m - 2, n - 1)
else:
    # k의 행, 열 위치 구하기
    k_row = (k - 1) // m + 1
    k_col = (k - 1) % m + 1
    
    # (1,1)에서 (k_row, k_col)까지의 경로 수
    first_part = comb(k_row + k_col - 2, k_row - 1)
    
    # (k_row, k_col)에서 (n, m)까지의 경로 수
    second_part = comb((n - k_row) + (m - k_col), n - k_row)
    
    answer = first_part * second_part

print(answer)
