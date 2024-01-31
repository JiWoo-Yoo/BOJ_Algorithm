from collections import defaultdict
t = int(input())
ani_s = defaultdict(str)
for _ in range(t):
    sound = input().split()
    while True:
        s = input()
        if s == 'what does the fox say?':
            break
        else:
            s = s.split()
            ani_s[s[0]] = s[2]
    for s in sound:
        if s not in ani_s.values():
            print(s, end=' ')
    print()
