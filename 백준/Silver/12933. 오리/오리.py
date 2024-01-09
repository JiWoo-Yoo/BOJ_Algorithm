def distin_ducks():
    duck_say = "quack"
    saying = input()
    quacks = 0 # 짖는수
    ducks = 0 # 오리 수
    if saying == duck_say * (len(saying) // len(duck_say)): # quack만 반복되면
        return 1
    else:
        list_saying = list(saying) # 리스트로 만듦: 문자를 바꾸기 위함
        while True: # 오리 구분 round
            # 종료조건 만들기
            if len(''.join(list_saying)) % len(duck_say) != 0: # 길이가 5의 배수가 아니면
                return -1
            if ''.join(list_saying) == '': # 전부 처리
                break
            i, j = 0, 0
            quacks = 0
            while i < len(list_saying): # 오리들의 말을 한글자씩 확인
                if list_saying[i] == duck_say[j]: # q,u,a,c,k 중 하나(처음엔q)
                    list_saying[i] = '' # 다음 turn에서 안 세도록 삭제
                    if j == len(duck_say) - 1: # 'k'면
                        quacks += 1 # 짖는소리 추가
                    j = (j + 1) % len(duck_say)
                i += 1
            if quacks > 0: # 한 번 이상 온전하게 짖었으면
                ducks += 1 # 오리 한마리 추가
            else: # 못 짖었다.
                return -1
        if ducks == 0: # 오리가 없으면
            ducks = -1 # 가능 오리 없음 반환
        return ducks
            
    
print(distin_ducks())
