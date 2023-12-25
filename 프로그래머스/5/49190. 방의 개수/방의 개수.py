from collections import defaultdict

def solution(arrows):
    rooms = 0
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    x, y = 0, 0
    path = defaultdict(list)

    for arrow in arrows:
        for i in range(2):  # 대각선 겹침을 위해 1씩 두번 이동
            nx, ny = x + dx[arrow], y + dy[arrow]  # 화살표 방향 위치 확인
            if (nx, ny) in path:  # 방문했던 점
                if (x, y) not in path[(nx, ny)]:  # 경로 안겹침
                    rooms += 1  # 방 생김(사이클)
                    path[(x, y)].append((nx, ny))
                    path[(nx, ny)].append((x, y))
            else:  # 방문 안한 점
                path[(x, y)].append((nx, ny))
                path[(nx, ny)].append((x, y))

            x, y = nx, ny  # 화살표 방향으로 이동

    return rooms
