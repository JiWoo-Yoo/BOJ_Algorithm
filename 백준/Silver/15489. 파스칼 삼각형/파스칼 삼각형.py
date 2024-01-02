def sum_triangle(r, c, w):
    # 파스칼 삼각형 만들기
    pascal_height = 30
    pascal = [[] for _ in range(pascal_height + 1)]
    for i in range(pascal_height):
        for j in range(i+1):
            if j == 0 or j == i:
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
    # 합 구하기
    answer = 0
    cnt = 0
    for i in range(r-1, r - 1 + w): # r행
        for j in range(c-1, c + cnt): # c열
            answer += pascal[i][j]
            # print(pascal[i][j], i, j)
        cnt += 1
    return answer
r, c, w = map(int, input().split())
print(sum_triangle(r, c, w))
