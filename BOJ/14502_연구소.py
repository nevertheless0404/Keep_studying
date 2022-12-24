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

        # 나가면 안돼!
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            visit[nx][ny] = 2
            virus(nx, ny)


# 안전영역 개수 구하기
def Cnt():
    count = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0:
                count += 1
    return count


def make_wall(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                visit[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if visit[i][j] == 2:
                    virus(i, j)
        result = max(result, Cnt())
        return
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    cnt += 1
                    make_wall(cnt)
                    graph[i][j] = 0
                    cnt -= 1


result = 0
make_wall(0)
print(result)
