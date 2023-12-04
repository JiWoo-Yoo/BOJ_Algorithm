from collections import deque

def solution(begin, target, words):
    answer = 0
    def can_change(before, after):
        diff_char = 0
        for i in range(len(before)):
            if before[i] != after[i]:
                diff_char += 1
            if diff_char > 1:
                return False
        return True
    
    def bfs():
        queue = deque()
        queue.append([begin, 0])
        
        if target not in words:
            return 0
        
        while queue:
            ch, distance = queue.popleft()
            if ch == target:
                return distance
            for word in words:
                if can_change(ch, word):
                    queue.append([word, distance + 1])
    answer = bfs()
    return answer