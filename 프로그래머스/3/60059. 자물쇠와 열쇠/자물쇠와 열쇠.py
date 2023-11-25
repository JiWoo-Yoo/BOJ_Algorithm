def rotate_90(key): # 90도 회전
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result

def check(big_lock): # 자물쇠가 열리는지 확인
    key_size = len(big_lock) // 3
    for i in range(key_size, key_size * 2):
        for j in range(key_size, key_size * 2):
            if big_lock[i][j] != 1:
                return False
    return True
    
def solution(key, lock):
    m = len(key)
    n = len(lock)
    big_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            big_lock[i + n][j + n] = lock[i][j]
    for rotation in range(4):
        key = rotate_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        big_lock[x+i][y+j] += key[i][j]
                if check(big_lock) == True:
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            big_lock[x+i][y+j] -= key[i][j]   
    return False