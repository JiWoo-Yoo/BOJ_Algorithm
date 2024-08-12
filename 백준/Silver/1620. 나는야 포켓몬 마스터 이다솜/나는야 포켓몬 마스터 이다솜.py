n, m = map(int, input().split())
num_po = {}
po_num = {}
for i in range(n):
    temp = input()
    po_num[temp] = i+1
    num_po[i+1] = temp

number = '0123456789'
for _ in range(m):
    question = input()
    if question[0] in number:
        print(num_po[int(question)])
    else:
        print(po_num[question])