# 수열과 연산자
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하기
# 순열 아이디어 https://zu-techlog.tistory.com/62
import sys
input = sys.stdin.readline
from itertools import permutations # 순열

n = int(input())
a = list(map(int, input().split()))

# +, -, *, /
oper_cnt = list(map(int, input().split()))

# 모든 연산자를 쭉 나열하기
opers = '+' * oper_cnt[0] + '-' * oper_cnt[1] + '*' * oper_cnt[2] + '/' * oper_cnt[3]

# 순열을 이용해 가능한 연산자 순서의 모든 조합을 나타냄
operator_perm = permutations(opers, n-1)

max_result = -int(1e9)
min_result = int(1e9)

for comb in operator_perm: # 가능한 조합을 하나씩 꺼내보고
    result = a[0]
    for i in range(1, n):
        if comb[i-1] == '+':
            result += a[i]
        elif comb[i-1] == '-':
            result -= a[i]
        elif comb[i-1] == '*':
            result *= a[i]
        elif comb[i-1] == '/':
            if result < 0 and a[i] > 0:
                result = -1 * (abs(result) // a[i])
            else:
                result //= a[i]
    max_result = max(max_result, result)
    min_result = min(min_result, result)
    
print(max_result)
print(min_result)
