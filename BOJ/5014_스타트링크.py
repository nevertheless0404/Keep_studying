# https://www.acmicpc.net/problem/5014

import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visit = [0 for _ in range(f + 1)]


def bfs():
    q = deque()
    q.append(s)
    visit[s] = 1

    while q:
        floor = q.popleft()
        if floor == g:
            return visit[g] - 1

        # up
        if floor + u <= f and not visit[floor + u]:
            q.append(floor + u)
            visit[floor + u] = visit[floor] + 1

        # down
        if floor - d >= 1 and not visit[floor - d]:
            q.append(floor - d)
            visit[floor - d] = visit[floor] + 1

    return "use the stairs"


print(bfs())
