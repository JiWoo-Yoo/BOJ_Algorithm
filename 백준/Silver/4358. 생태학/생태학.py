# 나무들이 주어졌을 때 각 종이 전체에서 차지하는 비율 구하기
from collections import defaultdict
trees = defaultdict(int) # 초기값 0
n = 0

# 입력 크기가 안주어짐: EOF
while True:
    try:
        treeName = input()
        trees[treeName] += 1
        n += 1
    except:
        break

keys = sorted(trees)
for key in keys:
    tree_cnt = trees[key]
    # # 곱셈먼저 한 뒤 round를 해야 4자릿수 나옴
    # percent = round((tree_cnt / n) * 100, 4)
    if n > 0:
        # print(key, percent)
        print("%s %.4f" % (key, tree_cnt/n * 100))
    else:
        print("error: divided into 0")