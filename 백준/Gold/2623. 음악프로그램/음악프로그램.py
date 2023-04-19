import sys
from collections import deque
input = sys.stdin.readline

# N = 가수의 수, M = 보조 PD의 수
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

indegree = [0] * (N + 1)

for _ in range(M):
    info = list(map(int, input().split()))
    for idx in range(info[0] - 1):
        graph[info[idx + 1]].append(info[idx + 2])
        indegree[info[idx + 2]] += 1

result = []
q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
    
while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)


if len(result) != N:
    print(0)
else:
    for singer in result:
        print(singer)