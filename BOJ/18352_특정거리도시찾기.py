# https://www.acmicpc.net/problem/18352

import sys

input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# -1로 초기화
visit = [-1] * (N + 1)


def bfs(v):
    q = deque()
    q.append(v)
    visit[v] = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            # 현재 노드의 연결 노드 중 미 방문 노드
            if visit[i] == -1:
                visit[i] = visit[v] + 1
                q.append(i)


for _ in range(M):
    s, e = map(int, input().split())
    # 그래프 인접 리스트에 그래프 데이터 저장
    graph[s].append(e)
bfs(X)

if K not in visit:
    print(-1)
else:
    for j in range(N + 1):
        if visit[j] == K:
            print(j)
