N, M = map(int, input().split())
nums = [i + 1 for i in range(N)]
out = []
visited = [False]*(N)

def dfs(cnt):
    if(cnt == M):
        print(*out)
        return
    for i in range(0, N):
        if visited[i]:
            continue
        visited[i] = True
        out.append(nums[i])
        dfs(cnt+1)
        out.pop()
        visited[i] = False
        
dfs(0)
