# stack 사용하기
def is_vps(ps):
    answer = ['NO', 'YES']
    stack = []
    for b in ps:
        if b == '(': # '('이면 스택에 넣다가 )를 만나면 pop.
            stack.append(b)
        elif b == ')':
            if len(stack) == 0: # 처음부터 )이면 NO return
                return answer[0]
            else:
                stack.pop()
    if len(stack) > 0: # 마지막에 (나 )가 남아있으면 NO return
        return answer[0]       
    return answer[1] # 스택에 아무것도 안남아있으면 YES return
    

t = int(input())
for _ in range(t):
    ps = input()
    print(is_vps(ps))

