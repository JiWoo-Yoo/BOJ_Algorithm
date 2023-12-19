def solution(money):
    if len(money) == 3:  # 길이가 3이면 하나밖에 못고름
        return max(money)
    
    first_steal_money = money[:-1]  # 첫 집을 터는 경우의 돈목록
    first_steal_money.append(0)
    
    last_steal_money = money[:]  # 마지막 집을 터는 경우의 돈목록
    last_steal_money[0] = 0
    
    first_steal_max = [0] * len(money)  # 첫 집을 터는 경우 돈의 최댓값
    last_steal_max = [0] * len(money)  # 마지막 집을 터는 경우 돈의 최댓값
    
    first_steal_max[0], first_steal_max[1] = first_steal_money[0], max(first_steal_money[0], first_steal_money[1])
    last_steal_max[0], last_steal_max[1] = last_steal_money[0], max(last_steal_money[0], last_steal_money[1])
    
    for i in range(2, len(money)-1):  # 첫 집을 터는 경우
        first_steal_max[i] = max(first_steal_max[i-1], first_steal_max[i-2] + first_steal_money[i])
        
    for i in range(2, len(money)):  # 마지막 집을 터는 경우
        last_steal_max[i] = max(last_steal_max[i-1], last_steal_max[i-2] + last_steal_money[i])
    
    answer = max(first_steal_max[-2], last_steal_max[-1])
    return answer
