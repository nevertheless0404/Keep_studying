import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque()
    q.append((0, 0))
    visit[0][0] = 0

    while q:
        x, y = q.popleft()
        if x == m - 1 and y == n - 1:
            return visit[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == -1:
                if data[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                else:
                    # 벽이 없는 곳을 만났을 때는 큐에서
                    # 먼저 가게 함
                    visit[nx][ny] = visit[x][y]
                    q.appendleft((nx, ny))


n, m = map(int, input().split())
data = [list(map(int, input().rstrip())) for _ in range(m)]
visit = [[-1] * n for _ in range(m)]

print(bfs())
