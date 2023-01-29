import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    princess = 10001

    q = deque()
    q.append((0, 0))
    visit[0][0] = 1

    while q:
        x, y = q.popleft()

        if graph[x][y] == 2:
            princess = abs(n - 1 - x) + abs(m - 1 - y) + visit[x][y] - 1

        if (x, y) == (n - 1, m - 1):
            return min(visit[x][y] - 1, princess)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and graph[nx][ny] != 1:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1

    return princess


n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

result = bfs()

if result <= t:
    print(result)
else:
    print("Fail")