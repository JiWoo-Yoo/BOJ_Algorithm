def dfs(computers, v, visited):
    visited[v] = True
    for i in range(len(computers[v])):
        if computers[v][i] == 1 and not visited[i]:
            dfs(computers, i, visited)
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                computers[i][j] = -1
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    return answer