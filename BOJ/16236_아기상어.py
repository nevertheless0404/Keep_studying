# https://www.acmicpc.net/problem/16236

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


x, y, size = 0, 0, 2
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, size):
    dist = [[0] * n for _ in range(n)]
    visit = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    tmp = []

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if graph[nx][ny] <= size:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[cx][cy] + 1

                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        tmp.append((nx, ny, dist[nx][ny]))

    # 거리가 가까운 물고기가 많으면 가장 왼쪽에 있는 물고기를 먹어!!!!
    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
result = 0
while True:
    shark = bfs(x, y, size)

    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    result += dist
    graph[x][y], graph[nx][ny] = 0, 0

    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(result)
