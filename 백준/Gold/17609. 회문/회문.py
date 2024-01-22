# 회문인지 검사
def is_palindrome(s):
    start, end = 0, len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

# 3개 검사
def pal_pseudo_not(s):
    length = len(s)
    
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]: # 다름
            if is_palindrome(s[:i] + s[i+1:]) or is_palindrome(s[:length-1-i] + s[length-i:]):
                return 1
            else:
                return 2
    # 아무것도 아님
    return 0
    
t = int(input())
for _ in range(t):
    s = input()
    print(pal_pseudo_not(s))
