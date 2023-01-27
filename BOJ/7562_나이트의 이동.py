# https://www.acmicpc.net/problem/7562

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if x == n and y == m:
            print(visit[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))


n = int(input())
for _ in range(n):
    l = int(input())
    visit = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    n, m = map(int, input().split())
    bfs(x, y)
