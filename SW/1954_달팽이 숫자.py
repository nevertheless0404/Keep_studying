# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq


t = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, t + 1):
    n = int(input())
    data = [[0] * n for _ in range(n)]
    # 초기 위치 및 회전 방향
    x, y = 0, 0
    dist = 0

    for j in range(1, n * n + 1):
        data[x][y] = j
        x += dx[dist]
        y += dy[dist]

        # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 으로
        # 인덱스를 다시 원위치 시켜줘야 하므로 뺌!
        # 다시 움직일 수 있도록 업데이트
        if not 0 <= x < n or not 0 <= y < n or data[x][y] != 0:
            x -= dx[dist]
            y -= dy[dist]
            # dist % 4 안해주면 0123, 4567 이렇게 커지므로 나머지로 접근
            dist = (dist + 1) % 4
            x += dx[dist]
            y += dy[dist]

    print("#%d" % i)
    for j in range(n):
        for k in range(n):
            print(data[j][k], end=" ")
        print()
