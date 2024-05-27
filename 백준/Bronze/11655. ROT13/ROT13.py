s = input()
answer = ''
number = '0123456789'
for c in s:
    if c in number or c == ' ':
        answer += c
    elif 'A' <= c <= 'Z':
        answer += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    elif 'a' <= c <= 'z':
        answer += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
print(answer)