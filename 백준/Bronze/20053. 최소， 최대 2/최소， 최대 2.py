t = int(input())

for _ in range(t):
    n = int(input())
    ints = list(map(int, input().split()))
    print(min(ints), max(ints))
