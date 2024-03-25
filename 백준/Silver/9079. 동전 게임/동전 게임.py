# 최소 뒤집기 연산으로 전체 동전을 똑같이 만들기
# 뒤집기 연산: 가로, 세로, 대각선 한번에 쭈루룩 바꾸기

# 속도 올리기
import sys
input = sys.stdin.readline

from collections import deque

def row_change(matrix, row):
    # 가로 연산
    for i in range(3):
        if matrix[row][i] == 1:
            matrix[row][i] = 0
        else:
            matrix[row][i] = 1
    return matrix
            
def col_change(matrix, col):
    # 세로 연산
    for i in range(3):
        if matrix[i][col] == 1:
            matrix[i][col] = 0
        else:
            matrix[i][col] = 1
    return matrix
            
def dia_change(matrix, state):
    # 대각선 연산
    if state == 1: # 증가
        for i in range(3):
            if matrix[i][i] == 1:
                matrix[i][i] = 0
            else:
                matrix[i][i] = 1
    else: # 감소
        for i in range(3):
            if matrix[2 - i][i] == 1:
                matrix[2 - i][i] = 0
            else:
                matrix[2 - i][i] = 1
    return matrix

def is_all_same(matrix):
    sum_m = 0
    for i in range(3):
        for j in range(3):
            sum_m += matrix[i][j]
    if sum_m == 9 or sum_m == 0:
        return True
    return False

def mat_to_int(matrix):
    bin_n = ''
    for row in matrix:
        for num in row:
            bin_n += str(num)
    bin_n = int(bin_n, 2)
    return bin_n
    
def int_to_mat(num):
    mat = [[0 for _ in range(3)] for i in range(3)]
    bin_n = str(bin(num))[2:].zfill(9)
    n_index = 0
    for i in range(3):
        for j in range(3):
            mat[i][j] = int(bin_n[n_index])
            n_index += 1
            
    return mat
    
    
def change_coin(matrix):
    visited = [False] * 512
    start = mat_to_int(matrix)
    q = deque([[start, 0]])
    visited[start] = True
    
    while q:
        [now, cnt] = q.popleft()
        
        now = int_to_mat(now)
        
        if is_all_same(now): # 다 같은 면이면
            return cnt
            
        # 아직 다 같은 면이 아니면
        
        # 행 연산
        for i in range(3):
            now = row_change(now, i)
            next_num = mat_to_int(now)
            if visited[next_num] == False:
                visited[next_num] = True
                q.append([next_num, cnt + 1])
            now = row_change(now, i)
            
        # 열 연산
        for i in range(3):
            now = col_change(now, i)
            next_num = mat_to_int(now)
            if visited[next_num] == False:
                visited[next_num] = True
                q.append([next_num, cnt + 1])
            now = col_change(now, i)
            
        # 대각선 연산
        for i in range(2):
            now = dia_change(now, i)
            next_num = mat_to_int(now)
            if visited[next_num] == False:
                visited[next_num] = True
                q.append([next_num, cnt + 1])
            now = dia_change(now, i)
                
    return -1

t = int(input())
for _ in range(t):
    # create 3x3 matrix
    matrix = []
    for i in range(3):
        temp_arr = input().split()
        for j in range(3):
            if temp_arr[j] == 'H':
                temp_arr[j] = 1
            else:
                temp_arr[j] = 0
        matrix.append(temp_arr)
    # 비트마스크: 1=h, 0=t
    answer = change_coin(matrix)
    print(answer)
