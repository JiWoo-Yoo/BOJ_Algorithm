import math
def solution(progresses, speeds):
#     progress[i] 완료하려면 speeds[i] * day1
#     progress[i+1] 완료하려면 speeds[i+1] * day2
    
#     day1 = 100 / speeds[i]
#     day2 = 100 / speeds[i+1]
    
#     즉, day 리스트를 구한뒤에
#     앞에서부터 같은 day인것들을 count

    req_days = [] # 배포까지 걸리는 일수
    answer = []
    
    for i in range(len(progresses)):
        rest_days = 100 - progresses[i]
        req_days.append(math.ceil(rest_days / speeds[i]))
    deploy_cnt = 0
    deploy_day = req_days[0]
    for days in req_days:
        if days <= deploy_day:
            deploy_cnt += 1
        else:
            answer.append(deploy_cnt)
            deploy_cnt = 1
            deploy_day = days
    answer.append(deploy_cnt)
    return answer