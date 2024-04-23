def solution(bandage, health, attacks):
    answer = health
    for i in range(len(attacks)):
        answer -= attacks[i][1] # 공격!
        print(answer, i)
        if answer <= 0: # 죽으면
            return -1
        if i == len(attacks) - 1: # 마지막 공격!
            break
        if attacks[i+1][0] - attacks[i][0] >= 2: # 연속치료성공
            if attacks[i+1][0] - attacks[i][0] < bandage[0]:
                answer += (attacks[i+1][0] - attacks[i][0] - 1) * bandage[1] # 공격사이 텀보다 붕대감기가 오래걸림: 감은 붕대만큼 체력 추가
            elif attacks[i+1][0] - attacks[i][0] >= bandage[0]:
                answer += (attacks[i+1][0] - attacks[i][0] - 1) * bandage[1] 
                answer += ((attacks[i+1][0] - attacks[i][0] - 1) // bandage[0]) * bandage[2] # 공격사이 텀보다 붕대감기가 짧게걸림: 감은붕대 + 추가체력 추가
            
        answer = min(answer, health)
            
    return answer