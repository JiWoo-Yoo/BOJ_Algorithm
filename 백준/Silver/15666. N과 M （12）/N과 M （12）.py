n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 비내림차순으로정렬
arr.sort()

# 2. dfs
out = []
def dfs(start):
    if len(out) == m:
        print(*out)
        return
    prev = 0
    for i in range(start, n):
        if prev != arr[i]:
            out.append(arr[i])
            prev = arr[i]
            dfs(i)
            out.pop()
        
dfs(0)