n, m = map(int, input().split())
friends = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(peer, path):
    if len(path) == 5:
        return 1
    for friend in friends[peer]:
        if friend not in path:
            path.append(friend)
            if dfs(friend, path):
                return 1
            path.pop()
    return 0

answer = 0
for i in range(n):
    if dfs(i, [i]):
        answer = 1
        break

print(answer)
