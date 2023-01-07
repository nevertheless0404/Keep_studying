import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


n, m = map(int, input().split())
island = [list(map(str, input().rstrip())) for _ in range(n)]
big_one = 0


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visit = [[0] * m for _ in range(n)]
    cnt = 0
    visit[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and island[nx][ny] == "L":
                    q.append((nx, ny))
                    # 갔던 곳 기준으로 이동거리 +1
                    visit[nx][ny] = visit[x][y] + 1
                    cnt = max(visit[nx][ny], cnt)
    return cnt - 1


for i in range(n):
    for j in range(m):
        # "L" 육지 탐색
        if island[i][j] == "L":
            big_one = max(bfs(i, j), big_one)

print(big_one)