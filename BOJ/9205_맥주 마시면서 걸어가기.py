# https://www.acmicpc.net/problem/9205

import sys
from collections import deque

input = sys.stdin.readline
beer = int(input().rstrip())

for _ in range(beer):
    n = int(input().rstrip())
    nx, ny = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    mx, my = map(int, input().split())
    visit = [0 for _ in range(n + 1)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.appendleft()
        if abs(x - nx) + abs(y - ny) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visit[i]:
                sx, sy = store[i]
                if abs(x - sx) + abs(y + sy) <= 1000:
                    q.append((sx, sy))
                    visit[i] = 1
