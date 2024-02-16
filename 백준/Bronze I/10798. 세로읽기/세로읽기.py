magnets = []
for _ in range(5):
    line = list(input())
    while len(line) < 15:
        line.append('')
    magnets.append(line)

for c in range(15):
    for r in range(5):
        if magnets[r][c] == '':
            continue
        print(magnets[r][c], end='')
        
