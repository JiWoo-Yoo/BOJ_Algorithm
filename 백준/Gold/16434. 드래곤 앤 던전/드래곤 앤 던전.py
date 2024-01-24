# 아이디어 참고: https://cochin-man.tistory.com/39

n, h_atk = map(int, input().split())

td = 0 # 누적 데미지
ta = h_atk # 공격력
max_hp = float("inf")

for i in range(n):
    t, a, h = map(int, input().split())
    if t == 1: # monster
        if h % ta == 0:
            td -= (h // ta - 1) * a
        else:
            td -= h // ta * a
        max_hp = min(td, max_hp)
                    
    else: # potion
        ta += a
        td += h
        if td > 0:
            td = 0
max_hp = min(td, max_hp)            
print(abs(max_hp) + 1)
