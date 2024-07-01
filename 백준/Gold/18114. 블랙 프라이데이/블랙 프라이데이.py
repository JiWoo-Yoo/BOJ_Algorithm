# 제시하는 양의 정수의 무게 C에 딱 맞게 물건 가져오면
# 전부 만 원에 판매
# -> 만 원에 구매할 수 있는 조합이 있으면 1 없으면 0
# 최대 3개까지 선택 가능

n, c = map(int, input().split())
w = list(map(int, input().split()))

def binary_search(start, end, diff):
    while start <= end:
        mid = (start + end) // 2
        if w[mid] == diff:
            return True
        elif w[mid] < diff:
            start = mid + 1
        else:
            end = mid - 1
    return False

answer = 0
if c in w:
    answer = 1
else:
    w.sort()
    left, right = 0, n - 1
    while left < right:
        l_sum_r = w[left] + w[right]
        if l_sum_r == c:
            answer = 1
            break
        elif l_sum_r > c:
            right -= 1
        else: # l + r < c
            diff = c - l_sum_r
            if w[left] != diff and w[right] != diff and binary_search(left, right, diff):
                answer = 1
                break 
            else:
                left += 1
        
print(answer)