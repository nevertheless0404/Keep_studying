import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global o, v

    q = deque()
    q.append((x, y))
    sheep = 0
    wolf = 0

    if road[x][y] == "o":
        sheep += 1
    elif road[x][y] == "v":
        wolf += 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < r
                and 0 <= ny < c
                and not visit[nx][ny]
                and road[nx][ny] != "#"
            ):
                if road[nx][ny] == "o":
                    sheep += 1
                if road[nx][ny] == "v":
                    wolf += 1

                visit[nx][ny] = 1
                q.append((nx, ny))

    if sheep and wolf:
        if sheep > wolf:
            v -= wolf
        else:
            o -= sheep


r, c = map(int, input().split())
road = []
visit = [[0] * c for _ in range(r)]
o, v = 0, 0

for i in range(r):
    a = list(input().strip())

    for j in range(c):
        if a[j] == "o":
            o += 1
        if a[j] == "v":
            v += 1
    road.append(a)

for i in range(r):
    for j in range(c):
        if (road[i][j] == "o" or road[i][j] == "v") and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i, j)
print(o, v)