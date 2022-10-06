# https://www.acmicpc.net/problem/1697

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [0] * 100001


def bfs():
    queue = deque([n])

    while queue:
        x = queue.popleft()

        # 현재 위치가 동생이랑 같은 위치이면 멈추고리
        # 그 자리위치를 알려줘
        if x == k:
            print(graph[x])
            break

        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= 100000 and not graph[i]:
                graph[i] = graph[x] + 1
                queue.append(i)


bfs()
