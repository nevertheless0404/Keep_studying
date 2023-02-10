import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
k = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def stra(start):
    q = []
    heappush(q, (0, start))
    dist[start] = 0

    while q:
        way, now = heappop(q)

        # 현재 노드가 이미 처리된 적 있는 노드라면 나와
        if dist[now] < way:
            continue

        for i in graph[now]:
            cost = way + i[1]
            # 다른 노드로 이동하는 거리가 더 짧을 때
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heappush(q, (cost, i[0]))


stra(k)

# 최단 거리
for i in range(1, n + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])