# https://www.acmicpc.net/problem/1987

import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(input()))
ans = 0
alpha = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny] in alpha:
            alpha.add(maps[nx][ny])
            dfs(nx, ny, cnt + 1)
            alpha.remove(maps[nx][ny])

alpha.add(maps[0][0])
dfs(0, 0, 1)
print(ans)
