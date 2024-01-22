n = int(input())
INF = int(1e9)
apb = 'abcdefghijklmnopqrstuvwxyz'
prop = [[INF] * len(apb) for i in range(len(apb))]


for i in range(n):
    p, q = input().split(' is ')
    prop[apb.index(p)][apb.index(q)] = 1
    
# 플루이드-워셜 알고리즘
for k in range(len(apb)):
    for a in range(len(apb)):
        for b in range(len(apb)):
            if a == b:
                prop[a][b] = 0
                continue
            if prop[a][k] == 1 and prop[k][b] == 1:
                prop[a][b] = 1

m = int(input())
for _ in range(m):
    p, q = input().split(' is ')
    if prop[apb.index(p)][apb.index(q)] == 1:
        print('T')
    else:
        print('F')
