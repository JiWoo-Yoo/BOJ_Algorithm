# 동전 NxM
# 앞0 뒤1
# 모든 동전을 앞면으로 만드는 동전 뒤집는 횟수 구하는 프로그램

n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append([])
    inp = input()
    for j in range(m):
        coin[i].append(int(inp[j]))
    
def flip(arr, a, b):
    for i in range(a+1):
        for j in range(b+1):
            if arr[i][j] == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    return arr

# 뒤부터 탐색하면서 1이면 뒤집기?
cnt = 0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if coin[i][j] == 1:
            coin = flip(coin, i, j)
            cnt += 1
            
print(cnt)