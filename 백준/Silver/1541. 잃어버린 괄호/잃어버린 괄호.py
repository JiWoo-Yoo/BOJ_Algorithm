# 괄호를 쳐서 최소로
eq = input()
minus_split = eq.split('-')
answer = 0

# +와 -만 있기 때문에 -뒤의 수에 괄호 치면 최소 
part_sum = sum(map(int, minus_split[0].split('+')))
if eq[0] == '-':
    answer -= part_sum
else:
    answer += part_sum
    
for i in range(1, len(minus_split)):
    part_sum = sum(map(int, minus_split[i].split('+')))
    answer -= part_sum

print(answer)
