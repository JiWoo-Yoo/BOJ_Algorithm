while True:
    try:
        # ROT13 -> 평문
        rot13 = input()
        
        # 모음 -> 오른쪽 3번: 왼쪽3번
        # 자음 -> 오른쪽 10번: 왼쪽10번
        
        answer = ''
        mo = 'aiyeou'
        ja = 'bkxznhdcwgpvjqtsrlmf'
        
        mo_upper = mo.upper()
        ja_upper = ja.upper()
        
        for c in rot13:
            if c in mo:
                index = mo.find(c)
                answer += mo[index-3]
            elif c in mo_upper:
                index = mo_upper.find(c)
                answer += mo_upper[index-3]
            elif c in ja:
                index = ja.find(c)
                answer += ja[index-10]
            elif c in ja_upper:
                index = ja_upper.find(c)
                answer += ja_upper[index-10]
            else:
                answer += c
        print(answer)
    except:
        break