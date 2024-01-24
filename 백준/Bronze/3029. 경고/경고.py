hh, mm, ss = map(int, input().split(':'))
Na_hh, Na_mm, Na_ss = map(int, input().split(':'))

# 분 단위로 바꾸기
t1 = hh*60*60 + mm*60 + ss
t2 = Na_hh*60*60 + Na_mm*60 + Na_ss

t = t2-t1 if t2 > t1 else t2-t1 + 24*60*60

h = t // 60// 60
m = t // 60 % 60
s = t % 60

print("%02d:%02d:%02d" % (h, m, s))
