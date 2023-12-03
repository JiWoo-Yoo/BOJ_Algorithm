def solution(numbers, target):
    answer = 0
    add = 0
    def dfs(index, add):
        nonlocal answer
        if index == len(numbers):
            if add == target:
                answer += 1
            return
        dfs(index + 1, add + numbers[index])
        dfs(index + 1, add - numbers[index])
        
    dfs(0, 0)
    return answer