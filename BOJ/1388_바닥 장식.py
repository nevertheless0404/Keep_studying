# https://www.acmicpc.net/problem/1388

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]


def dfs(x, y):
    if graph[x][y] == "|":
        graph[x][y] = 1
        for x_ in [1, -1]:
            X = x + x_
            if (X > 0 and X < n) and graph[X][y] == "|":
                dfs(X, y)

    if graph[x][y] == "-":
        graph[x][y] = 1
        for y_ in [1, -1]:
            Y = y + y_
            if (Y > 0 and Y < m) and graph[x][Y] == "-":
                dfs(x, Y)


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "-" or graph[i][j] == "|":
            dfs(i, j)
            cnt += 1

print(cnt)
