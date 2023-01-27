# https://www.acmicpc.net/problem/9205

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((home_x, home_y))
    while q:
        x, y = q.popleft()
        if abs(x - fest_x) + abs(y - fest_y) <= 1000:
            print("happy")
            return
        for i in range(n):  # 편의점들 확인
            if not visit[i]:  # 편의점을 방문하지 않았다면
                new_x, new_y = graph[i]  # 편의점의 좌표를 새로 뽑고
                if abs(x - new_x) + abs(y - new_y) <= 1000:  # 다음거리까지 갈 수 있다면
                    visit[i] = 1  # 방문체크
                    q.append((new_x, new_y))
    print("sad")
    return


t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    graph = []
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))
    fest_x, fest_y = map(int, input().split())
    visit = [0 for _ in range(n + 1)]
    bfs()
