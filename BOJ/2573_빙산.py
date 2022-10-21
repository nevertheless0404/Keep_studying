# https://www.acmicpc.net/problem/2573

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    visit[a][b] = True
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and not visit[nx][ny] == 0:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                elif not maps[nx][ny]:
                    water[x][y] += 1
    return 1


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

year, flag = 0, 0

while True:
    visit = [[0] * m for _ in range(n)]
    water = [[0] * m for _ in range(n)]
    land_cnt = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] and not visit[i][j]:
                bfs(i, j)
                land_cnt += 1
    for i in range(n):
        for j in range(m):
            maps[i][j] -= water[i][j]
            if maps[i][j] < 0:
                maps[i][j] = 0
    if land_cnt == 0:
        break
    if land_cnt >= 2:
        flag = 1
        break
    year += 1
if flag:
    print(year)
else:
    print(0)
