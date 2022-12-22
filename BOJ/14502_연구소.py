# https://www.acmicpc.net/problem/14502

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 나가지 않게 하기!
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            visit[nx][ny] = 2
            virus(nx, ny)
