def solution(number, k):
    stack = []
    answer = ''
    
    for i, num in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        
        stack.append(num)

    # 남은 k만큼 제거 (예: 54321, k=2인 경우 543를 선택)
    stack = stack[:-k] if k > 0 else stack

    answer = ''.join(stack)
    return answer