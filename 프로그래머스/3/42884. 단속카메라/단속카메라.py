def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])  # 이탈 지점을 기준으로 정렬

    camera_position = float('-inf')

    for route in routes:
        if camera_position < route[0]:  # 현재 카메라 위치보다 더 뒤에 있는 경우에만 카메라 설치
            answer += 1
            camera_position = route[1]

    return answer
