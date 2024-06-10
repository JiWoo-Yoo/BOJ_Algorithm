# 문자열에서 빈번하게 나타나는 알파벳 출력
t = int(input())
for i in range(t):
    s = input()
    
    apb = list(set(s))
    
    apb_data = dict()
    
    for ch in apb:
        apb_data[ch] = 0
    
    for ch in s:
        if ch != ' ':
            apb_data[ch] += 1
    
    apb_cnt = sorted(apb_data.values(), reverse=True)
        
    if len(apb_cnt) > 1 and apb_cnt[0] == apb_cnt[1] or len(apb_cnt) == 0:
        answer = "?"
    else:
        answer = max(apb_data, key=apb_data.get)
    
    print(answer)