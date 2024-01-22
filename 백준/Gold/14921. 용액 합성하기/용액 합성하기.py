# 투포인터 알고리즘

def comb_liq():
    n = int(input())
    a = list(map(int, input().split()))
    l1, l2 = 0, n - 1
    min_diff = float('inf')
    while l1 < l2:
        plus = a[l1] + a[l2]
        if abs(plus) < abs(min_diff):
            min_diff = plus     
        if plus > 0:
            l2 -= 1
        elif plus < 0:
            l1 += 1
        else:
            break
    
    return min_diff

print(comb_liq())
