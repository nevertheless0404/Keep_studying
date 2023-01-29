import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
self_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append([nx, ny])


for i in range(101):
    visit = [[0] * n for i in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] <= i:
                visit[j][k] = 1

    for j in range(n):
        for k in range(n):
            if visit[j][k] == 0:
                visit[j][k] = 1
                bfs(j, k)
                cnt += 1

    if cnt == 0:
        break
    self_cnt = max(self_cnt, cnt)

print(self_cnt)