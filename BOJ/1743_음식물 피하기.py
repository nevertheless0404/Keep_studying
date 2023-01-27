# https://www.acmicpc.net/problem/1743

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    # 그래프 인덱스는 0 부터 시작해서 -1를 해준다음 쓰레기 위치 표시
    graph[a - 1][b - 1] = 1

visit = [[0] * m for _ in range(n)]
result = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visit[i][j]:
            cnt = 0
            bfs(i, j)
            result = max(result, cnt)

print(result)
