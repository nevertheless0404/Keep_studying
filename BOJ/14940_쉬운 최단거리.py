# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))

    visit[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
                # 갈 수 없는 땅
                if graph[nx][ny] == 0:
                    visit[nx][ny] = 0
                # 갈 수 있는 땅
                elif graph[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))


n, m = map(int, input().split())
visit = [[-1] * m for _ in range(n)]

graph = []
x, y = 0, 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            x, y = i, j

    graph.append(row)

bfs(x, y)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=" ")
        else:
            print(visit[i][j], end=" ")

    print()
