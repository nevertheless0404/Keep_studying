# https://www.acmicpc.net/problem/1916

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
visit = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def bfs(start):
    q = []
    heappush(q, (0, start))
    visit[start] = 0

    while q:
        dist, now = heappop(q)
        if visit[now] < dist:
            continue

        for i in graph[now]:
            nc = dist + i[1]
            if nc < visit[i[0]]:
                visit[i[0]] = nc
                heappush(q, (nc, i[0]))


bfs(start)
print(visit[end])
