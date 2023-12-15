# stack을 이용
s = input()
stack = []
answer = ''
is_tag = False
for i in range(len(s)):
    if is_tag:
        if s[i] == '>':
            is_tag = False
        answer += s[i]
    elif not is_tag:
        if s[i] == '<':
            if len(stack) > 0:
                while len(stack) > 0:
                    answer += stack.pop()
            is_tag = True
            answer += s[i]
        elif s[i] == ' ':
            while len(stack) > 0:
                answer += stack.pop()
            answer += s[i]
        else:
            stack.append(s[i])
while len(stack) > 0:
    answer += stack.pop()
print(answer)
