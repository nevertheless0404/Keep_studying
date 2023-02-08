# https://www.acmicpc.net/problem/11779

import sys
from collections import deque
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
visit = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
x, y = map(int, input().split())


def stra(start):
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    visit[start] = start

    while q:
        way, now = heappop(q)
        if dist[now] < way:
            continue

        for end, cost in graph[now]:
            n_way = way + cost
            if dist[end] > n_way:
                dist[end] = n_way
                visit[end] = now
                heappush(q, (n_way, end))


stra(x)

dq = deque([])
arr = []
dq.append(y)

while dq:
    now = dq.popleft()
    arr.append(now)
    if now == x:
        break

    dq.append(visit[now])

print(dist[y])
print(len(arr))
print(*arr[::-1])
