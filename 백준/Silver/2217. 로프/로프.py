n = int(input())
ws = []
for _ in range(n):
    ws.append(int(input()))
    
ws.sort(reverse=True)
max_sum = ws[0] # 가장 큰 중량을 버틸수있는녀석

for k in range(2, len(ws) + 1):
    now_sum = ws[k-1] * k
    if max_sum < now_sum:
        max_sum = now_sum
    
print(max_sum)
