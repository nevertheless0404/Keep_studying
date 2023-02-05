import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque([n])

    while q:
        x = q.popleft()
        if x == k:
            return visit[x]

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < 100001 and not visit[nx]:
                if nx == 2 * x and x != 0:
                    visit[nx] = visit[x]
                    q.appendleft(nx)
                else:
                    visit[nx] = visit[x] + 1
                    q.append(nx)


n, k = map(int, input().split())
visit = [0] * 100001

print(bfs())